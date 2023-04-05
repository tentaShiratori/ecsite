"""
This type stub file was generated by pyright.
"""

import logging
import requests
from io import IOBase
from typing import Any, IO, Iterator, List, Optional, Tuple
from botocore.model import OperationModel

logger: logging.Logger
class StreamingBody(IOBase):
    def __init__(self, raw_stream: IO[bytes], content_length: int) -> None:
        ...
    
    def set_socket_timeout(self, timeout: float) -> None:
        ...
    
    def readable(self) -> bool:
        ...
    
    def read(self, amt: Optional[int] = ...) -> bytes:
        ...
    
    def readlines(self) -> List[bytes]:
        ...
    
    def __iter__(self) -> Iterator[bytes]:
        ...
    
    def iter_lines(self, chunk_size: int = ..., keepends: bool = ...) -> Iterator[bytes]:
        ...
    
    def iter_chunks(self, chunk_size: int = ...) -> Iterator[bytes]:
        ...
    
    def tell(self) -> int:
        ...
    
    def close(self) -> None:
        ...
    
    def next(self) -> bytes:
        ...
    


def get_response(operation_model: OperationModel, http_response: requests.Response) -> Tuple[requests.Response, Any]:
    ...
