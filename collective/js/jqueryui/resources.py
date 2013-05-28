import logging
from copy import copy
from zope import component
from StringIO import StringIO
try:
    from zope.component.hooks import getSite
except ImportError:
    #BBB
    from zope.site.hooks import getSite
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
from Products.ResourceRegistries.tools.packer import CSSPacker
from Products.ResourceRegistries.tools.packer import JavascriptPacker
from Products.ResourceRegistries.utils import applyPrefix

from collective.js.jqueryui import interfaces, config

from Acquisition import aq_parent
logger = logging.getLogger('collective.js.jqueryui')


class Resources(BrowserView):
    _key = None
    _header_template = u"\n/* collective.js.jqueryui: %s */\n"
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
                self._tool = getToolByName(self.context,
                                           self._toolid)
            else:
                self._tool = False
        return self._tool

    @property
    def debug(self):
        ret = False
        if self.tool:
            ret = self.tool.getDebugMode()
        return ret

    def settings(self):
        """Return records from portal_registry corresponding to
        IJQueryUIPlugins
        """
        registry = component.queryUtility(IRegistry)
        if registry is None or self._key is None:
            return
        return registry.forInterface(self._key, None)

    def __call__(self):
        settings = self.settings
        if settings is None:
            return
        resources = self.get_resources()
        if self._mimetype:
            self.request.response.setHeader('Content-Type',
                                            self._mimetype)
        if resources is None:
            resources = ""
        return self.get_resources_content(resources)

    def pack(self, content):
        if self._packer and not self.debug:
            return self._packer('safe').pack(content)
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
                resource = self.context.restrictedTraverse(
                    resourceid)
            except KeyError, e:
                logger.error(e)
                continue
            if not resource:
                continue
            if self._header_template:
                data.write(
                    self._header_template % (
                        resource.context.__name__
                    )
                )
                data.write(u"\n")

            # read the content of the resource
            fic = open(resource.context.path, 'r')
            content = fic.read()
            fic.close()
            try:
                content = unicode(content)

            except Exception, e:
                content = unicode(content.decode('utf-8'))

            #css applyPrefix
            if self._css:
                upath = upath.rstrip('/')
                prefix = '/'.join([upath, resourceid])
                if prefix.endswith('/'):
                    prefix = prefix[:-1]
                prefix = '/'.join(
                    prefix.split('/')[:-1])
                content = applyPrefix(content, prefix)

            #content is already minified
            data.write(content)
            data.write(u"\n")

        return data.getvalue()


class JQueryUICustomJS(Resources):
    """This view aggregate javascripts according to the configuration. It has
    been created to not polute the portal_javascripts will all plugins"""
    _js = True
    _css = False
    _key = interfaces.IJQueryUIPlugins
    _mimetype = 'application/javascript'
    _toolid = 'portal_javascripts'
    _packer = JavascriptPacker

    def get_resources(self):
        """Return a list of resources (at least their ids) computed from
        the configuration provided by IJQueryUIPlugins's records in plone
        portal_registry"""
        settings = self.settings()
        deps = config.JQUERYUI_DEPENDENCIES
        alljs = deps.keys()
        resources = []
        wanted = []  # not ordered list of wanted plugins
        tpl = "++resource++jquery-ui/jquery.%s.min.js"
        ordered_plugins = copy(config.ORDERED_PLUGINS)
        for plugin in alljs:
            attr_name = plugin.replace('.', '_').replace('-', '_')
            is_wanted = getattr(settings, attr_name, False)
            if is_wanted:
                wanted.append(plugin)
                deps = config.JQUERYUI_DEPENDENCIES[plugin]
                for dep in deps:
                    wanted.append(dep)
        for plugin in alljs:
            if plugin not in wanted:
                ordered_plugins.remove(plugin)
        for plugin in ordered_plugins:
            resources.append(tpl % plugin)
            if plugin == 'ui.datepicker':
                resources.append('++resource++jquery-ui-i18n.js')
        return resources


class JQueryUICustomCSS(Resources):
    """ . """
    _key = interfaces.IJQueryUICSS
    _mimetype = 'text/css'
    _toolid = 'portal_css'
    _packer = CSSPacker
    _js = False
    _css = True

    def get_resources(self):
        """Return a list of resources (at least their ids) computed from
        the configuration provided by IJQueryUIPlugins's records in plone
        portal_registry"""
        settings = self.settings()
        resources_items = [
            ("css", config.CSS_RESOURCE_ID),
            ("patch", config.PATCH_RESOURCE_ID)]
        resources = []
        for skey, cssid in resources_items:
            if getattr(settings, skey, None):
                resources.append(cssid)
        return resources
