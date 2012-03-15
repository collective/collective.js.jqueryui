import logging
from copy import copy
from zope import component
try:
    from zope.component.hooks import getSite
except ImportError:
    #BBB
    from zope.site.hooks import getSite
from plone.registry.interfaces import IRegistry, IRecordModifiedEvent
from Products.Five import BrowserView
from StringIO import StringIO

from collective.js.jqueryui import interfaces, config

logger = logging.getLogger('collective.js.jqueryui')

class JQueryUICustomJS(BrowserView):
    """This view aggregate javascripts according to the configuration. It has
    been created to not polute the portal_javascripts will all plugins"""
    
    def __call__(self):
        settings = self.settings

        if settings is None:
            return
        resources = self.get_resources()

        if not resources:
            return

        return self.get_resources_content(resources)

    def settings(self):
        """Return records from portal_registry corresponding to IJQueryUIPlugins
        """
        registry = component.queryUtility(IRegistry)

        if registry is None:
            return

        return registry.forInterface(interfaces.IJQueryUIPlugins, None)

    def get_resources(self):
        """Return a list of resources (at least their ids) computed from
        the configuration provided by IJQueryUIPlugins's records in plone
        portal_registry"""
        settings = self.settings()
        deps = config.JQUERYUI_DEPENDENCIES
        all = deps.keys()
        resources = []
        wanted = [] #not ordered list of wanted plugins
        tpl = "++resource++jquery-ui/jquery.%s.min.js"
        ordered_plugins = copy(config.ORDERED_PLUGINS)

        for plugin in all:
            attr_name = plugin.replace('.','_')
            is_wanted = getattr(settings, attr_name, False)

            if is_wanted:
                wanted.append(plugin)
                deps = config.JQUERYUI_DEPENDENCIES[plugin]
                for dep in deps:
                    wanted.append(dep)

        for plugin in all:
            if plugin not in wanted:
                ordered_plugins.remove(plugin)

        for plugin in ordered_plugins:
            resources.append(tpl%plugin)
            if plugin == 'ui.datepicker':
                resources.append('++resource++jquery-ui-i18n.js')

        return resources


    def get_resources_content(self, resources):
        """Resources must be a list of resource ids.
        This method return the content of each resources appended in one string
        """
        data = StringIO()

        if resources is None:
            resources = self.get_resources()


        for resourceid in resources:
            try:
                resource = self.context.restrictedTraverse(resourceid)
            except KeyError,e:
                logger.error(e)
                continue

            if not resource:
                continue

            data.write(open(resource.context.path).read())
 
        return data.getvalue()

@component.adapter(interfaces.IJQueryUIPlugins, IRecordModifiedEvent)
def cook_js_resources(record, event):
    site=getSite()
    jsregistry = site.portal_javascripts
    jsregistry.cookResources()
