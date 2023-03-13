from django.test import TestCase,override_settings
from src.models import Product
import shutil

@override_settings(MEDIA_ROOT=('./test/media'))
class ProductTestCase(TestCase):
    def test_cant_create_without_image(self):
        p = Product(description="world",price=1.22)
        p.save()
        
def tearDownModule():
    try:
        shutil.rmtree("./test")
    except OSError:
        pass