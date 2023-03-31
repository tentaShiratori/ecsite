from mypy_boto3_s3 import S3Client
from injector import inject
from dataclasses import dataclass
from typing import IO, Any, cast
from django.conf import settings
from django.core.files import File


@inject
@dataclass
class FileUploader:
    client: S3Client
    bucket = "unko"

    @property
    def host(self):
        return settings.S3_HOST_ENDPOINT + self.bucket + "/"

    def run(self, fileObj: File, fileName: str):
        self.client.upload_fileobj(cast(Any, fileObj), self.bucket, fileName)
