from django.core.management.base import BaseCommand, CommandError
from src.models import Product, User
from django.core.files import File


class Command(BaseCommand):
    help = "Setup Dummy"

    def handle(self, *args, **options):
        u = User()
        u.save()
        p = Product(
            user=u,
            name="hello",
            description="world",
            price=1.3234,
            image="asdfa3289073240989",
        )
        p.save()
