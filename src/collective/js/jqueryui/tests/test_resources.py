# -*- coding: utf-8 -*-
from collective.js.jqueryui.testing import COLLECTIVE_JS_JQUERYUI_INTEGRATION_TESTING

import unittest


class TestJQueryUICustomJS(unittest.TestCase):

    layer = COLLECTIVE_JS_JQUERYUI_INTEGRATION_TESTING

    def test_get_resources(self):
        """The enabled plugins are aggregated, the core one first."""
        portal = self.layer["portal"]
        view = portal.restrictedTraverse("collective.js.jqueryui.custom.min.js")
        resources = view.get_resources()
        self.assertEqual(resources[0], "++resource++jquery-ui/jquery.ui.core.min.js")
        self.assertIn("++resource++jquery-ui/jquery.ui.widget.min.js", resources)
        self.assertIn("/* collective.js.jqueryui: jquery.ui.core.min.js */", view())
