import boto3
from mypy_boto3_s3.client import S3Client
import environ

env = environ.Env()
env.read_env(".env")


def get_s3_client() -> S3Client:
    return boto3.client("s3", endpoint_url=env("S3_ENDPOINT"))


class MyS3Client:
    s3client: S3Client

    def __init__(self) -> None:
        self.s3client = get_s3_client()

    @property
    def s3_host(self):
        return "http://localhost:4566/unko/"

    def upload_fileobj(self, fileObj, fileName):
        self.s3client.upload_fileobj(fileObj, "unko", fileName)
