from zope import component
from Products.CMFCore.utils import getToolByName
from plone.registry.interfaces import IRegistry
PROFILE = 'profile-collective.js.jqueryui:default'


def common(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILE)

    #cleanup from 1.8
    registry = component.queryUtility(IRegistry)
    for i in ('core','blind', 'bounce', 'clip', 'drop', 'explode',
              'fade', 'fold', 'highlight', 'pulsate', 'scale',
              'shake', 'slide', 'transfer'):
        record_id = 'collective.js.jqueryui.controlpanel.IJQueryUIPlugins.effects_%s'%i
        if record_id in registry.records:
            del registry.records[record_id]
        record_id = 'collective.js.jqueryui.controlpanel.IJQueryUIPlugins.ui_effects_%s'%i
        if record_id in registry.records:
            del registry.records[record_id]
