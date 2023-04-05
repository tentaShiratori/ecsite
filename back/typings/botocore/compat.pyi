"""
This type stub file was generated by pyright.
"""

from http.client import HTTPMessage
from logging import Logger
from typing import Any, Iterable, Mapping, Optional, Pattern, Tuple, Type, TypeVar
from xml.etree import ElementTree as ETree

logger: Logger = ...
_R = TypeVar("_R")
class HTTPHeaders(HTTPMessage):
    @classmethod
    def from_dict(cls: Type[_R], d: Mapping[str, Any]) -> _R:
        ...
    
    @classmethod
    def from_pairs(cls: Type[_R], pairs: Iterable[Tuple[str, Any]]) -> _R:
        ...
    


file_type: Any
unquote_str = ...
def set_socket_timeout(http_response: Any, timeout: Any) -> None:
    ...

def accepts_kwargs(func: Any) -> Any:
    ...

def ensure_unicode(s: Any, encoding: Optional[Any] = ..., errors: Optional[Any] = ...) -> Any:
    ...

def ensure_bytes(s: Any, encoding: str = ..., errors: str = ...) -> Any:
    ...

XMLParseError = ETree.ParseError
def filter_ssl_warnings() -> None:
    ...

from_dict = ...
from_pairs = ...
def copy_kwargs(kwargs: Any) -> Any:
    ...

def total_seconds(delta: Any) -> Any:
    ...

MD5_AVAILABLE: bool
def get_md5(*args: Any, **kwargs: Any) -> Any:
    ...

def compat_shell_split(s: Any, platform: Optional[Any] = ...) -> Any:
    ...

def get_tzinfo_options() -> Any:
    ...

HAS_CRT: bool
disabled: str
IPV4_PAT: str
IPV4_RE: Pattern[str]
HEX_PAT: str
LS32_PAT: str
UNRESERVED_PAT: str
IPV6_PAT: str
ZONE_ID_PAT: str
IPV6_ADDRZ_PAT: str
IPV6_ADDRZ_RE: Pattern[str]
UNSAFE_URL_CHARS: frozenset[str]
HAS_GZIP: bool