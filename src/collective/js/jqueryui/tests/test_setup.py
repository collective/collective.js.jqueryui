# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.js.jqueryui.testing import COLLECTIVE_JS_JQUERYUI_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.CMFPlone.browser.admin import AddPloneSite

import unittest


HAS_INSTALLER = True
try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    HAS_INSTALLER = False


class TestSetup(unittest.TestCase):
    """Test that collective.js.jqueryui is properly installed."""

    layer = COLLECTIVE_JS_JQUERYUI_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if HAS_INSTALLER:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if collective.js.jqueryui is installed."""
        if HAS_INSTALLER:
            self.assertTrue(
                self.installer.is_product_installed("collective.js.jqueryui")
            )
        else:
            self.assertTrue(self.installer.isProductInstalled("collective.js.jqueryui"))

    def test_browserlayer(self):
        """Test that IJqueryUILayer is registered."""
        from collective.js.jqueryui.interfaces import IJqueryUILayer
        from plone.browserlayer import utils

        self.assertIn(IJqueryUILayer, utils.registered_layers())

    def test_hide_extensions_profiles(self):
        if HAS_INSTALLER:
            return
        app = self.layer["app"]
        request = self.layer["request"]
        add_plone_site = AddPloneSite(app, request)
        profiles = add_plone_site.profiles()
        extensions_profiles = profiles["extensions"]
        profiles_ids = [profile["id"] for profile in extensions_profiles]
        jqueryui_profiles = [
            profile_id
            for profile_id in profiles_ids
            if profile_id.startswith("collective.js.jqueryui")
        ]
        self.assertEqual(["collective.js.jqueryui:default"], jqueryui_profiles)


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_JS_JQUERYUI_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        if HAS_INSTALLER:
            self.installer = get_installer(self.portal, self.layer["request"])
            self.installer.uninstall_product("collective.js.jqueryui")
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
            self.installer.uninstallProducts(["collective.js.jqueryui"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.js.jqueryui is cleanly uninstalled."""
        if HAS_INSTALLER:
            self.assertFalse(
                self.installer.is_product_installed("collective.js.jqueryui")
            )
        else:
            self.assertFalse(
                self.installer.isProductInstalled("collective.js.jqueryui")
            )

    def test_browserlayer_removed(self):
        """Test that IJqueryUILayer is removed."""
        from collective.js.jqueryui.interfaces import IJqueryUILayer
        from plone.browserlayer import utils

        self.assertNotIn(IJqueryUILayer, utils.registered_layers())
