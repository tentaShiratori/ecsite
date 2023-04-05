"""
This type stub file was generated by pyright.
"""

from collections.abc import MutableMapping
from logging import Logger
from typing import Any, Dict, Iterator, Mapping, Optional, Type, TypeVar
from botocore.compat import HTTPHeaders as HTTPHeaders, HTTPResponse as HTTPResponse
from urllib3.connection import HTTPConnection, VerifiedHTTPSConnection
from urllib3.connectionpool import HTTPConnectionPool, HTTPSConnectionPool

_R = TypeVar("_R")
logger: Logger = ...
class AWSHTTPResponse(HTTPResponse):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        ...
    


class AWSConnection:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        ...
    
    def close(self) -> None:
        ...
    
    def send(self, str: str) -> Any:
        ...
    


class AWSHTTPConnection(AWSConnection, HTTPConnection):
    ...


class AWSHTTPSConnection(AWSConnection, VerifiedHTTPSConnection):
    ...


class AWSHTTPConnectionPool(HTTPConnectionPool):
    ConnectionCls: Type[AWSHTTPConnection]
    ...


class AWSHTTPSConnectionPool(HTTPSConnectionPool):
    ConnectionCls: Type[AWSHTTPSConnection]
    ...


def prepare_request_dict(request_dict: Dict[str, Any], endpoint_url: str, context: Optional[Any] = ..., user_agent: Optional[Any] = ...) -> None:
    ...

def create_request_object(request_dict: Dict[str, Any]) -> Any:
    ...

class AWSPreparedRequest:
    def __init__(self, method: str, url: str, headers: HTTPHeaders, body: str, stream_output: bool) -> None:
        ...
    
    def reset_stream(self) -> None:
        ...
    


class AWSRequest:
    def __init__(self, method: Optional[str] = ..., url: Optional[str] = ..., headers: Optional[Mapping[str, Any]] = ..., data: Optional[Any] = ..., params: Optional[Dict[str, Any]] = ..., auth_path: Optional[str] = ..., stream_output: bool = ...) -> None:
        ...
    
    def prepare(self) -> AWSPreparedRequest:
        ...
    
    @property
    def body(self) -> str:
        ...
    


class AWSRequestPreparer:
    def prepare(self, original: AWSRequest) -> AWSPreparedRequest:
        ...
    


class AWSResponse:
    def __init__(self, url: str, status_code: int, headers: HTTPHeaders, raw: Any) -> None:
        ...
    
    @property
    def content(self) -> bytes:
        ...
    
    @property
    def text(self) -> str:
        ...
    


class _HeaderKey:
    def __init__(self, key: str) -> None:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other: Any) -> bool:
        ...
    


class HeadersDict(MutableMapping[str, str]):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        ...
    
    def __setitem__(self, key: str, value: Any) -> None:
        ...
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def __delitem__(self, key: str) -> None:
        ...
    
    def __iter__(self) -> Iterator[str]:
        ...
    
    def __len__(self) -> int:
        ...
    
    def copy(self: _R) -> _R:
        ...
    

