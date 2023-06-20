from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from Products.Five import BrowserView
from six import StringIO

import logging
import os
import re

from collective.js.jqueryui import config


logger = logging.getLogger("collective.js.jqueryui")

URL_MATCH = re.compile(
    r"""(url\s*\(\s*['"]?)(?!data:)([^'")]+)(['"]?\s*\))""",
    re.I | re.S,
)


def makeAbsolute(path, prefix):
    """Make a url into an absolute URL by applying the given prefix"""

    # Absolute path or full url
    if path.startswith("/") or "://" in path:
        return path

    absolute = "{0}/{1}".format(prefix, path)
    if "://" in absolute:
        return absolute

    normalized = os.path.normpath(absolute)
    if os.path.sep != "/":
        normalized = normalized.replace(os.path.sep, "/")
    return normalized


def applyPrefix(cssSource, prefix):
    """Return a copy of the string cssSource with each url() expression that
    contains an absolute path turned into an absolute path, by applying the
    given prefix.
    """
    if prefix.endswith("/"):
        prefix = prefix[:-1]

    return URL_MATCH.sub(
        lambda m: m.group(1) + makeAbsolute(m.group(2), prefix) + m.group(3),
        cssSource,
    )


class Resources(BrowserView):
    _header_template = "\n/* collective.js.jqueryui: %s */\n"
    _mimetype = None
    _tool = None
    _toolid = None
    _packer = None
    _js = False
    _css = False

    @property
    def tool(self):
        if self._tool is None:
            if self._toolid:
                self._tool = getToolByName(self.context, self._toolid)
            else:
                self._tool = False
        return self._tool

    @property
    def debug(self):
        ret = False
        if self.tool:
            ret = self.tool.getDebugMode()
        return ret

    def __call__(self):
        resources = self.get_resources()
        if self._mimetype:
            self.request.response.setHeader("Content-Type", self._mimetype)
        if resources is None:
            resources = ""
        return self.get_resources_content(resources)

    def pack(self, content):
        if self._packer and not self.debug:
            return self._packer("safe").pack(content)
        return content

    def get_resources_content(self, resources):
        """Resources must be a list of resource ids.
        This method return the content of each resources appended in one string
        """
        data = StringIO()
        if resources is None:
            resources = self.get_resources()
        upath = self.context.absolute_url_path()
        for resourceid in resources:
            try:
                resource = self.context.restrictedTraverse(resourceid)
            except KeyError as e:
                logger.error(e)
                continue
            if not resource:
                continue
            if self._header_template:
                data.write(self._header_template % (resource.context.__name__))
                data.write("\n")

            # read the content of the resource
            fic = open(resource.context.path, "r")
            content = fic.read()
            fic.close()
            content = safe_unicode(content)

            # css applyPrefix
            if self._css:
                upath = upath.rstrip("/")
                prefix = "/".join([upath, resourceid])
                if prefix.endswith("/"):
                    prefix = prefix[:-1]
                prefix = "/".join(prefix.split("/")[:-1])
                content = applyPrefix(content, prefix)

            # content is already minified
            data.write(content)
            data.write("\n")

        return data.getvalue()


class JQueryUICustomJS(Resources):
    """This view aggregate javascripts according to the configuration. It has
    been created to not polute the portal_javascripts will all plugins"""

    _js = True
    _css = False
    _mimetype = "application/javascript"
    _toolid = "portal_javascripts"
    # _packer = JavascriptPacker

    def get_resources(self):
        """Return a list of resources (at least their ids)."""
        resources = list(config.JQUERYUI_RESOURCES)
        # add i18n for datepicker, maybe it still works
        # resources.append('++resource++jquery-ui-i18n.js')
        return resources


class JQueryUICustomCSS(Resources):
    """."""

    _mimetype = "text/css"
    _toolid = "portal_css"
    # _packer = CSSPacker
    _js = False
    _css = True

    def get_resources(self):
        """Return a list of resources."""
        resources = list(config.CSS_RESOURCES)
        # and the CSS patch file
        resources.append("++resource++jquery-ui-themes/sunburst-patch.css")
        return resources
