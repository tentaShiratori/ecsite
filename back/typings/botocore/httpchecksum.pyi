"""
This type stub file was generated by pyright.
"""

import logging
from typing import Any, Dict, IO, Iterator, Mapping, Optional, Sequence, Type, Union
from botocore.awsrequest import AWSHTTPResponse
from botocore.model import OperationModel
from botocore.response import StreamingBody as StreamingBody

logger: logging.Logger
class BaseChecksum:
    def update(self, chunk: Union[bytes, bytearray]) -> None:
        ...
    
    def digest(self) -> bytes:
        ...
    
    def b64digest(self) -> str:
        ...
    
    def handle(self, body: Union[bytes, bytearray, IO[Any]]) -> str:
        ...
    


class Crc32Checksum(BaseChecksum):
    def __init__(self) -> None:
        ...
    


class CrtCrc32Checksum(BaseChecksum):
    def __init__(self) -> None:
        ...
    


class CrtCrc32cChecksum(BaseChecksum):
    def __init__(self) -> None:
        ...
    


class Sha1Checksum(BaseChecksum):
    def __init__(self) -> None:
        ...
    


class Sha256Checksum(BaseChecksum):
    def __init__(self) -> None:
        ...
    


class AwsChunkedWrapper:
    def __init__(self, raw: IO[Any], checksum_cls: Optional[Type[BaseChecksum]] = ..., checksum_name: str = ..., chunk_size: Optional[int] = ...) -> None:
        ...
    
    def seek(self, offset: int, whence: int = ...) -> None:
        ...
    
    def read(self, size: Optional[int] = ...) -> bytes:
        ...
    
    def __iter__(self) -> Iterator[bytes]:
        ...
    


class StreamingChecksumBody(StreamingBody):
    def __init__(self, raw_stream: IO[Any], content_length: int, checksum: BaseChecksum, expected: str) -> None:
        ...
    
    def read(self, amt: Optional[int] = ...) -> bytes:
        ...
    


def resolve_checksum_context(request: Dict[str, Any], operation_model: OperationModel, params: Mapping[str, Any]) -> None:
    ...

def resolve_request_checksum_algorithm(request: Dict[str, Any], operation_model: OperationModel, params: Mapping[str, Any], supported_algorithms: Optional[Sequence[str]] = ...) -> None:
    ...

def apply_request_checksum(request: Dict[str, Any]) -> None:
    ...

def resolve_response_checksum_algorithms(request: Dict[str, Any], operation_model: OperationModel, params: Mapping[str, Any], supported_algorithms: Optional[Sequence[str]] = ...) -> None:
    ...

def handle_checksum_body(http_response: AWSHTTPResponse, response: Dict[str, Any], context: Mapping[str, Any], operation_model: OperationModel) -> None:
    ...
