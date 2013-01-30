from zope import component
from Products.CMFCore.utils import getToolByName
from plone.registry.interfaces import IRegistry
PROFILE = 'profile-collective.js.jqueryui:default'


def common(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILE)

    #cleanup from 1.8
    registry = component.queryUtility(IRegistry)
    effect = 'collective.js.jqueryui.controlpanel.IJQueryUIPlugins.effects_%s'
    ui = 'collective.js.jqueryui.controlpanel.IJQueryUIPlugins.ui_effects_%s'
    for i in ('core', 'blind', 'bounce', 'clip', 'drop', 'explode',
              'fade', 'fold', 'highlight', 'pulsate', 'scale',
              'shake', 'slide', 'transfer'):
        record_id = effect % i
        if record_id in registry.records:
            del registry.records[record_id]
        record_id = ui % i
        if record_id in registry.records:
            del registry.records[record_id]

    css = getToolByName(context, 'portal_css')
    css.cookResources()
    js = getToolByName(context, 'portal_javascripts')
    js.cookResources()
