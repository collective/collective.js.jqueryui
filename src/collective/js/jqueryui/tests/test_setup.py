# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.js.jqueryui.testing import COLLECTIVE_JS_JQUERYUI_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.js.jqueryui is properly installed."""

    layer = COLLECTIVE_JS_JQUERYUI_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if collective.js.jqueryui is installed."""
        self.assertTrue(self.installer.is_product_installed("collective.js.jqueryui"))

    def test_browserlayer(self):
        """Test that IJqueryUILayer is registered."""
        from collective.js.jqueryui.interfaces import IJqueryUILayer
        from plone.browserlayer import utils

        self.assertIn(IJqueryUILayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_JS_JQUERYUI_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer = get_installer(self.portal, self.layer["request"])
        self.installer.uninstall_product("collective.js.jqueryui")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.js.jqueryui is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("collective.js.jqueryui"))

    def test_browserlayer_removed(self):
        """Test that IJqueryUILayer is removed."""
        from collective.js.jqueryui.interfaces import IJqueryUILayer
        from plone.browserlayer import utils

        self.assertNotIn(IJqueryUILayer, utils.registered_layers())
