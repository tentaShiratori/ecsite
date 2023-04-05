"""
This type stub file was generated by pyright.
"""

from logging import Logger
from typing import Any, Dict, List, Optional, Union
from botocore import waiter as waiter
from botocore.config import Config as Config
from botocore.history import HistoryRecorder
from botocore.hooks import BaseEventHooks
from botocore.loaders import Loader
from botocore.model import ServiceModel as ServiceModel
from botocore.paginate import Paginator as Paginator
from botocore.regions import BaseEndpointResolver, EndpointRulesetResolver
from botocore.serialize import Serializer
from botocore.signers import RequestSigner
from botocore.utils import CachedProperty as CachedProperty

logger: Logger = ...
history_recorder: HistoryRecorder = ...
class ClientCreator:
    def __init__(self, loader: Loader, endpoint_resolver: BaseEndpointResolver, user_agent: str, event_emitter: BaseEventHooks, retry_handler_factory: Any, retry_config_translator: Any, response_parser_factory: Optional[Any] = ..., exceptions_factory: Optional[Any] = ..., config_store: Optional[Any] = ...) -> None:
        ...
    
    def create_client(self, service_name: str, region_name: str, is_secure: bool = ..., endpoint_url: Optional[str] = ..., verify: Optional[Union[str, bool]] = ..., credentials: Optional[Any] = ..., scoped_config: Optional[Any] = ..., api_version: Optional[str] = ..., client_config: Optional[Config] = ..., auth_token: Optional[str] = ...) -> BaseClient:
        ...
    
    def create_client_class(self, service_name: str, api_version: Optional[Any] = ...) -> None:
        ...
    


class ClientEndpointBridge:
    DEFAULT_ENDPOINT: str = ...
    def __init__(self, endpoint_resolver: BaseEndpointResolver, scoped_config: Optional[Any] = ..., client_config: Optional[Any] = ..., default_endpoint: Optional[str] = ..., service_signing_name: Optional[str] = ..., config_store: Any = ..., service_signature_version: Optional[str] = ...) -> None:
        ...
    
    def resolve(self, service_name: str, region_name: Optional[str] = ..., endpoint_url: Optional[str] = ..., is_secure: bool = ...) -> None:
        ...
    
    def resolver_uses_builtin_data(self) -> bool:
        ...
    


class BaseClient:
    def __init__(self, serializer: Serializer, endpoint: str, response_parser: Any, event_emitter: BaseEventHooks, request_signer: RequestSigner, service_model: ServiceModel, loader: Loader, client_config: Config, partition: str, exceptions_factory: Any, endpoint_ruleset_resolver: Optional[EndpointRulesetResolver] = ...) -> None:
        ...
    
    def close(self) -> None:
        ...
    
    def get_paginator(self, operation_name: Any) -> Paginator:
        ...
    
    def can_paginate(self, operation_name: str) -> bool:
        ...
    
    def get_waiter(self, waiter_name: Any) -> waiter.Waiter:
        ...
    
    @CachedProperty
    def waiter_names(self) -> List[str]:
        ...
    
    @property
    def exceptions(self) -> Any:
        ...
    


class ClientMeta:
    def __init__(self, events: BaseEventHooks, client_config: Config, endpoint_url: str, service_model: ServiceModel, method_to_api_mapping: Dict[str, str], partition: str) -> None:
        ...
    
    @property
    def service_model(self) -> ServiceModel:
        ...
    
    @property
    def region_name(self) -> str:
        ...
    
    @property
    def endpoint_url(self) -> str:
        ...
    
    @property
    def config(self) -> Any:
        ...
    
    @property
    def method_to_api_mapping(self) -> Dict[str, str]:
        ...
    
    @property
    def partition(self) -> str:
        ...
    

