from django.core.management.base import BaseCommand
from catalog.models import Author, Country
from django_seed import Seed


class Command(BaseCommand):
    help = 'Generates 5 random countries and 100 random authors'

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        seeder.add_entity(Country, 5, {
            'name': lambda x: seeder.faker.country()
        })
        seeder.execute()
        countries = Country.objects.all()

        if not countries.exists():
            raise ValueError

        seeder.add_entity(Author, 100, {
            'first_name': lambda x: seeder.faker.first_name(),
            'last_name': lambda x: seeder.faker.last_name(),
            'pseudonym': lambda x: seeder.faker.user_name(),
            'date_of_birth': lambda x: seeder.faker.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=100),
            'country': lambda x: seeder.faker.random_element(elements=countries)
        })

        seeder.execute()
        print("Okey bla bla bla")
