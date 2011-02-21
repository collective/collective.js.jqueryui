from Products.CMFCore.utils import getToolByName

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
