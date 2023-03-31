from django.test import TestCase
from injector import Injector
from src.tests.di import test_modules
from src.drivers.aws.file_uploader import FileUploader
from django.core.files import File


class TestFileUploader(TestCase):
    injector: Injector

    def setUp(self):
        self.injector = Injector(test_modules)

    def test_can_upload_to_s3(self):
        file_uploader = self.injector.get(FileUploader)
        file_uploader.run(File(open(__file__)), "test.txt")
