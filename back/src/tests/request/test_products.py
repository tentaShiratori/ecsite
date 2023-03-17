from django.test import TestCase
from src.models import Product
from rest_framework.test import APIClient
import json
from django.core.files import File
import shutil
from django.test import override_settings


# Using the standard RequestFactory API to create a form POST request
@override_settings(MEDIA_ROOT=("./test/media"))
class ProductsRequestTestCase(TestCase):
    def setUp(self):
        p = Product(name="hello", description="world", price=1.23)
        p.image.save(
            "test_image.jpg",
            File(open("./fixture/image/aaa.jpg", "rb")),
        )
        p.save()

    def test_cant_create_without_image(self):
        factory = APIClient()
        response = factory.get("/products/")
        data = json.loads(response.content.decode())
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "hello")
        self.assertEqual(data[0]["description"], "world")
        self.assertEqual(data[0]["price"], 1.23)
        self.assertEqual(data[0]["image"], "/images/images/test_image.jpg")


def tearDownModule():
    try:
        shutil.rmtree("./test")
    except OSError:
        pass
