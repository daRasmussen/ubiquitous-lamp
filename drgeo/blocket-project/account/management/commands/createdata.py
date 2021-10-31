import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker

CATEGORIES = [
    "Shoes",
    "Shirts"
]

PRODUCTS = [
    "Shoes",
    "Shirts"
]


class Provider(faker.providers.BaseProvider):
    def ecommerce_category(self):
        return self.random_element(CATEGORIES)

    def ecommerce_products(self):
        return self.random_element(PRODUCTS)


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker(["sv_SE"])
        # print(fake.address())
        fake.add_provider(Provider)
        # print(fake.ecommerce_products())

        #print(fake.profile(fields=["username"]))
        #print(fake.profile(fields=["mail"]))
        #print(fake.password())
        for p in range(20):
            profile = fake.profile()
            print(profile["username"])
