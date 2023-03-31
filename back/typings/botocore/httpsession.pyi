"""
This type stub file was generated by pyright.
"""

from logging import Logger
from typing import Any, Optional

logger: Logger = ...
DEFAULT_TIMEOUT: int
MAX_POOL_CONNECTIONS: int
DEFAULT_CA_BUNDLE: Any
def get_cert_path(verify: Any) -> Any:
    ...

def create_urllib3_context(ssl_version: Optional[Any] = ..., cert_reqs: Optional[Any] = ..., options: Optional[Any] = ..., ciphers: Optional[Any] = ...) -> Any:
    ...

def ensure_boolean(val: Any) -> bool:
    ...

def mask_proxy_url(proxy_url: str) -> str:
    ...

class ProxyConfiguration:
    def __init__(self, proxies: Optional[Any] = ..., proxies_settings: Optional[Any] = ...) -> None:
        ...
    
    def proxy_url_for(self, url: Any) -> Any:
        ...
    
    def proxy_headers_for(self, proxy_url: Any) -> Any:
        ...
    
    @property
    def settings(self) -> Any:
        ...
    


class URLLib3Session:
    def __init__(self, verify: bool = ..., proxies: Optional[Any] = ..., timeout: Optional[Any] = ..., max_pool_connections: Any = ..., socket_options: Optional[Any] = ..., client_cert: Optional[Any] = ..., proxies_config: Optional[Any] = ...) -> None:
        ...
    
    def close(self) -> None:
        ...
    
    def send(self, request: Any) -> Any:
        ...
    


