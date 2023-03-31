from django.core.management.base import BaseCommand, CommandError
from src.models import Product, User


class Command(BaseCommand):
    help = "Setup Dummy"

    def handle(self, *args, **options):
        print([user.email for user in (User.objects.all())])
