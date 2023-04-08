from django.core.management.base import BaseCommand, CommandError
from src.models import Product, User, client


class Command(BaseCommand):
    help = "Setup Dummy"

    def handle(self, *args, **options):
        client.Client(sub="", email="foobar@gmail.com", first_name="").save()
        print([user.email for user in (User.objects.all())])
