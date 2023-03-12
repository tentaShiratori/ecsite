from django.core.management.base import BaseCommand, CommandError
from src.models import Product
from django.core.files import File

class Command(BaseCommand):
    help = "Setup Dummy"

    def handle(self, *args, **options):
        p = Product(name="hello",description="world",price=1.3234)
        p.image.save("abc.jpg",File(open("./dummy/aaa.jpg","rb")))