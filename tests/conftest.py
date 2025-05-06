# from collective.geolocationbehavior.geolocation import IGeolocatable
from collective.schedulefield.testing import FUNCTIONAL_TESTING
from collective.schedulefield.testing import INTEGRATION_TESTING
from pytest_plone import fixtures_factory


pytest_plugins = ["pytest_plone"]


globals().update(
    fixtures_factory(
        (
            (FUNCTIONAL_TESTING, "functional"),
            (INTEGRATION_TESTING, "integration"),
        )
    )
)
