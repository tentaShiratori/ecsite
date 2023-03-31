"""
This type stub file was generated by pyright.
"""

import sys
from logging import Logger
from typing import Any, Dict, List, Optional, TypedDict, Union
from botocore.client import ClientEndpointBridge
from botocore.config import Config as Config
from botocore.configprovider import ConfigValueStore
from botocore.endpoint import Endpoint
from botocore.hooks import BaseEventHooks
from botocore.loaders import Loader
from botocore.model import ServiceModel
from botocore.parsers import ResponseParser, ResponseParserFactory
from botocore.serialize import BaseRestSerializer
from botocore.signers import RequestSigner as RequestSigner

if sys.version_info >= (3, 9):
    ...
else:
    ...
logger: Logger = ...
VALID_REGIONAL_ENDPOINTS_CONFIG: List[str]
LEGACY_GLOBAL_STS_REGIONS: List[str]
class _GetClientArgsTypeDef(TypedDict):
    serializer: BaseRestSerializer
    endpoint: Endpoint
    response_parser: ResponseParser
    event_emitter: BaseEventHooks
    request_signer: RequestSigner
    service_model: ServiceModel
    loader: Loader
    client_config: Config
    partition: Optional[str]
    exceptions_factory: Any
    ...


class ClientArgsCreator:
    def __init__(self, event_emitter: BaseEventHooks, user_agent: Any, response_parser_factory: ResponseParserFactory, loader: Loader, exceptions_factory: Any, config_store: ConfigValueStore) -> None:
        ...
    
    def get_client_args(self, service_model: ServiceModel, region_name: str, is_secure: bool, endpoint_url: Optional[str], verify: Optional[Union[str, bool]], credentials: Optional[Any], scoped_config: Optional[Dict[str, Any]], client_config: Optional[Config], endpoint_bridge: ClientEndpointBridge, auth_token: Optional[str] = ..., endpoints_ruleset_data: Optional[Dict[str, Any]] = ..., partition_data: Optional[Dict[str, Any]] = ...) -> _GetClientArgsTypeDef:
        ...
    
    def compute_client_args(self, service_model: ServiceModel, client_config: Optional[Config], endpoint_bridge: ClientEndpointBridge, region_name: str, endpoint_url: str, is_secure: bool, scoped_config: Optional[Dict[str, Any]]) -> Any:
        ...
    
    def compute_s3_config(self, client_config: Optional[Config]) -> Dict[str, Any]:
        ...
    
    def compute_endpoint_resolver_builtin_defaults(self, region_name: str, service_name: str, s3_config: Dict[str, Any], endpoint_bridge: ClientEndpointBridge, client_endpoint_url: str, legacy_endpoint_url: str) -> Dict[str, Any]:
        ...
    


