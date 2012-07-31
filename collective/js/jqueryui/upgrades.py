from Products.CMFCore.utils import getToolByName
from zope.component.interfaces import ComponentLookupError


def install_browserlayer(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'browserlayer', run_dependencies=False,
                                   purge_old=False)

PREVIOUS = ('++resource++jquery-ui-1.8.min.js',
            '++resource++jquery-ui-1.7.min.js',
            '++resource++jquery-ui-1.7.2.min.js')


def portal_javascripts(context):

    jsregistry = getToolByName(context, 'portal_javascripts')
    for PREV in PREVIOUS:
        jsregistry.unregisterResource(PREV)

    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'jsregistry', run_dependencies=False,
                                   purge_old=False)


def cook_resources(context):
    """Refresh javascript and css"""
    jsregistry = getToolByName(context, 'portal_javascripts')
    cssregistry = getToolByName(context, 'portal_css')

    jsregistry.cookResources()
    cssregistry.cookResources()


def renaming_css_browserresource_188_189(context):
    cssregistry = getToolByName(context, 'portal_css')
    jsregistry = getToolByName(context, 'portal_javascripts')
    setup = getToolByName(context, 'portal_setup')

    cssregistry.unregisterResource('++resource++jquery.ui.all.css')
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'jsregistry', run_dependencies=False,
                                   purge_old=False)
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'cssregistry', run_dependencies=False,
                                   purge_old=False)

    jsregistry.cookResources()
    cssregistry.cookResources()


def upgrade_1890_1891(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'jsregistry', run_dependencies=False,
                                   purge_old=False)
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'cssregistry', run_dependencies=False,
                                   purge_old=False)
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'propertiestool', run_dependencies=False,
                                   purge_old=False)


def upgrade_1891_1892(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'jsregistry', run_dependencies=False,
                                   purge_old=False)
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'cssregistry', run_dependencies=False,
                                   purge_old=False)
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'propertiestool', run_dependencies=False,
                                   purge_old=False)


def upgrade_1892_1893(context):
    """remove ++resource++jquery-ui-themes/sunburst/jquery-ui-1.8.9.custom.css
    apply css profile and cook javascript resource"""
    cssregistry = getToolByName(context, 'portal_css')
    setup = getToolByName(context, 'portal_setup')

    rid = '++resource++jquery-ui-themes/sunburst/jquery-ui-1.8.9.custom.css'
    cssregistry.unregisterResource(rid)
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'jsregistry', run_dependencies=False,
                                   purge_old=False)
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'cssregistry', run_dependencies=False,
                                   purge_old=False)


def upgrade_1893_1894(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'propertiestool', run_dependencies=False,
                                   purge_old=False)


def upgrade_1894_1895(context):
    setup = getToolByName(context, 'portal_setup')
    cssregistry = getToolByName(context, 'portal_css')
    rid = '++resource++jquery-ui-themes/sunburst/jquery-ui-1.8.12.custom.css'
    removes = (rid, '++resource++jquery-ui-themes/sunburst-patch.css')
    for remove in removes:
        cssregistry.unregisterResource(remove)

    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'cssregistry', run_dependencies=False,
                                    purge_old=False)


def upgrade_1896_1898(context):
    jsregistry = getToolByName(context, 'portal_javascripts')
    cssregistry = getToolByName(context, 'portal_css')

    setup = getToolByName(context, 'portal_setup')

    jsregistry.unregisterResource('++resource++jquery-ui.min.js')
    # will be readdded
    jsregistry.unregisterResource('++resource++jquery-ui-i18n.js')
    rids = ('++resource++jquery-ui-themes/sunburst/jqueryui.css',
            '++resource++jquery-ui-themes/sunburst-patch.css')
    for rid in rids:
        cssregistry.unregisterResource(rid)

    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'jsregistry', run_dependencies=False,
                                   purge_old=False)
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'cssregistry', run_dependencies=False,
                                   purge_old=False)
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'actions', run_dependencies=False,
                                   purge_old=False)
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'controlpanel', run_dependencies=False,
                                   purge_old=False)

    #We choose to activate all plugins for compatibility purpose.
    #but we need to be sure plone.app.registry is installed
    from zope.component import getUtility
    from plone.registry.interfaces import IRegistry
    #is plone.app.registry
    try:
        registry = getUtility(IRegistry)
    except ComponentLookupError:
        profile = 'profile-plone.app.registry:default'
        setup.runAllImportStepsFromProfile(profile)

    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                                   'plone.app.registry',
                                   run_dependencies=False,
                                   purge_old=False)


def upgrade_1898_1899(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                               'collective.js.jqueryui',
                               run_dependencies=False,
                               purge_old=False)


def upgrade_1899_1900(context):
    jsregistry = getToolByName(context, 'portal_javascripts')
    base = '++resource++jquery-ui/jquery.'
    plugins = ['ui.core', 'ui.widget', 'ui.mouse', 'ui.position',
               'ui.draggable', 'ui.droppable', 'ui.resizable', 'ui.selectable',
               'ui.sortable', 'ui.accordion', 'ui.autocomplete', 'ui.button',
               'ui.dialog', 'ui.slider', 'ui.tabs', 'ui.datepicker',
               'ui.progressbar', 'effects.core', 'effects.blind',
               'effects.bounce', 'effects.clip', 'effects.drop',
               'effects.explode', 'effects.fade', 'effects.fold',
               'effects.highlight', 'effects.pulsate', 'effects.scale',
               'effects.shake', 'effects.slide', 'effects.transfer']
    for plugin in plugins:
        jsregistry.unregisterResource('%s%s.min.js' % (base, plugin))

    jsregistry.unregisterResource('++resource++jquery-ui-i18n.js')

    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                               'jsregistry', run_dependencies=False,
                               purge_old=False)

    jsregistry.cookResources()


def upgrade_1900_2000(context):
    cssregistry = getToolByName(context, 'portal_css')
    ids = ['++resource++jquery-ui-themes/sunburst/jqueryui.css',
           '++resource++jquery-ui-themes/sunburst-patch.css']
    resourcesids = cssregistry.getResourceIds()
    for i in ids:
        if i in resourcesids:
            cssregistry.unregisterResource(i)
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(
        'profile-collective.js.jqueryui:default',
        'cssregistry',
        run_dependencies=False,
        purge_old=False)
    cssregistry.cookResources()

def upgrade_2000_2100(context):
    jsregistry = getToolByName(context, 'portal_javascripts')
    cssregistry = getToolByName(context, 'portal_css')
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(
        'profile-collective.js.jqueryui:default',
        'cssregistry',
        run_dependencies=False,
        purge_old=False)
    cssregistry.cookResources()

def upgrade_2100_2200(context):
    jsregistry = getToolByName(context, 'portal_javascripts')
    cssregistry = getToolByName(context, 'portal_css')
    setup = getToolByName(context, 'portal_setup')
    cssregistry.cookResources()

