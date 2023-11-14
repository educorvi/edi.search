# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import edi.search


class EdiSearchLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=edi.search)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'edi.search:default')


EDI_SEARCH_FIXTURE = EdiSearchLayer()


EDI_SEARCH_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDI_SEARCH_FIXTURE,),
    name='EdiSearchLayer:IntegrationTesting',
)


EDI_SEARCH_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDI_SEARCH_FIXTURE,),
    name='EdiSearchLayer:FunctionalTesting',
)


EDI_SEARCH_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EDI_SEARCH_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='EdiSearchLayer:AcceptanceTesting',
)
