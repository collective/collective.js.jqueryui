from zope.component._api import getUtility
from plone.registry.interfaces import IRegistry

from collective.js.jqueryui.interfaces import IJQueryUIPlugins
from collective.js.jqueryui.controlpanel import verify_jsregistry

def applySettings(gscontext):
    # don't run as a step for other profiles
    if gscontext.readDataFile('jqueryui.txt') is None:
        return

    record = getUtility(IRegistry).forInterface(IJQueryUIPlugins)

    verify_jsregistry(record)
