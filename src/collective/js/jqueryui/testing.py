# -*- coding: utf-8 -*-
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer

import collective.js.jqueryui


class CollectiveJsJqueryuiLayer(PloneSandboxLayer):
    def setUpZope(self, app, configurationContext):  # @UnusedVariable
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.js.jqueryui)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.js.jqueryui:default")


COLLECTIVE_JS_JQUERYUI_FIXTURE = CollectiveJsJqueryuiLayer()


COLLECTIVE_JS_JQUERYUI_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_JS_JQUERYUI_FIXTURE,),
    name="CollectiveJsJqueryuiLayer:IntegrationTesting",
)


COLLECTIVE_JS_JQUERYUI_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_JS_JQUERYUI_FIXTURE,),
    name="CollectiveJsJqueryuiLayer:FunctionalTesting",
)
