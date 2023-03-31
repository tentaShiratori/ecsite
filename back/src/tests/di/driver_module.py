from injector import Module, provider
from src.drivers.aws.file_uploader import FileUploader
from mypy_boto3_s3 import S3Client
from typing import IO, Any
from dataclasses import dataclass


@dataclass
class MockFileUploader(FileUploader):
    def run(self, fileObj: IO[Any], fileName: str):
        print("run file uploader")


class MockDriverModule(Module):
    @provider
    def mock_file_uploader(self, client: S3Client) -> FileUploader:
        return MockFileUploader(client)
