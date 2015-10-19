# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import pythonjam.site


class PythonjamSiteLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=pythonjam.site)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'pythonjam.site:default')


PYTHONJAM_SITE_FIXTURE = PythonjamSiteLayer()


PYTHONJAM_SITE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PYTHONJAM_SITE_FIXTURE,),
    name='PythonjamSiteLayer:IntegrationTesting'
)


PYTHONJAM_SITE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PYTHONJAM_SITE_FIXTURE,),
    name='PythonjamSiteLayer:FunctionalTesting'
)


PYTHONJAM_SITE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PYTHONJAM_SITE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PythonjamSiteLayer:AcceptanceTesting'
)
