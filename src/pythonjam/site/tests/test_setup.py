# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from pythonjam.site.testing import PYTHONJAM_SITE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that pythonjam.site is properly installed."""

    layer = PYTHONJAM_SITE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if pythonjam.site is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'pythonjam.site'))

    def test_browserlayer(self):
        """Test that IPythonjamSiteLayer is registered."""
        from pythonjam.site.interfaces import (
            IPythonjamSiteLayer)
        from plone.browserlayer import utils
        self.assertIn(IPythonjamSiteLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PYTHONJAM_SITE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['pythonjam.site'])

    def test_product_uninstalled(self):
        """Test if pythonjam.site is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'pythonjam.site'))

    def test_browserlayer_removed(self):
        """Test that IPythonjamSiteLayer is removed."""
        from pythonjam.site.interfaces import IPythonjamSiteLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPythonjamSiteLayer, utils.registered_layers())
