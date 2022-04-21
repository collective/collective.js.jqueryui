# -*- coding: utf-8 -*-
from collective.js.jqueryui.controlpanel import IJQueryUIPlugins
from collective.js.jqueryui.controlpanel import verify_jsregistry
from plone.registry.interfaces import IRegistry
from Products.CMFPlone import interfaces as Plone
from Products.CMFQuickInstallerTool import interfaces as QuickInstaller
from zope.component._api import getUtility
from zope.interface import implementer


def applySettings(gscontext):
    # don't run as a step for other profiles
    if gscontext.readDataFile("jqueryui.txt") is None:
        return
    record = getUtility(IRegistry).forInterface(IJQueryUIPlugins)
    verify_jsregistry(record)


@implementer(Plone.INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Do not show on Plone's list of installable profiles."""
        return [
            "collective.js.jqueryui:install-base",
            "collective.js.jqueryui:uninstall",
            "collective.js.jqueryui:uninstall-base",
        ]


@implementer(QuickInstaller.INonInstallable)
class HiddenProducts(object):
    def getNonInstallableProducts(self):
        """Do not show on QuickInstaller's list of installable products."""
        return []
