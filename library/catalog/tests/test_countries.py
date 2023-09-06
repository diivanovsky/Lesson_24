from django.test import TestCase
from catalog.models import Country


class CountryStrTestCase(TestCase):
    fixtures = ['catalog/tests/fixtures/countries_fixture.json']

    def test_str_representation(self):
        country = Country.objects.get(id=1)
        self.assertEqual(country.name, str(country))


