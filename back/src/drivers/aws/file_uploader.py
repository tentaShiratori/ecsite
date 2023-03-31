from mypy_boto3_s3 import S3Client
from injector import inject
from dataclasses import dataclass
from typing import IO, Any
from django.conf import settings


@inject
@dataclass
class FileUploader:
    client: S3Client

    @property
    def host(self):
        return settings.S3_ENDPOINT

    def run(self, fileObj: IO[Any], fileName: str):
        self.client.upload_fileobj(fileObj, "unko", fileName)
