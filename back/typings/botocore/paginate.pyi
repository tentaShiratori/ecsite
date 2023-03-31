"""
This type stub file was generated by pyright.
"""

from logging import Logger
from typing import Any, Iterator

log: Logger = ...
class TokenEncoder:
    def encode(self, token: Any) -> Any:
        ...
    


class TokenDecoder:
    def decode(self, token: Any) -> Any:
        ...
    


class PaginatorModel:
    def __init__(self, paginator_config: Any) -> None:
        ...
    
    def get_paginator(self, operation_name: Any) -> Any:
        ...
    


class PageIterator:
    def __init__(self, method: Any, input_token: Any, output_token: Any, more_results: Any, result_keys: Any, non_aggregate_keys: Any, limit_key: Any, max_items: int, starting_token: Any, page_size: int, op_kwargs: Any) -> None:
        ...
    
    @property
    def result_keys(self) -> Any:
        ...
    
    @property
    def resume_token(self) -> Any:
        ...
    
    @resume_token.setter
    def resume_token(self, value: Any) -> None:
        ...
    
    @property
    def non_aggregate_part(self) -> Any:
        ...
    
    def __iter__(self) -> Iterator[Any]:
        ...
    
    def search(self, expression: Any) -> Iterator[Any]:
        ...
    
    def result_key_iters(self) -> Any:
        ...
    
    def build_full_result(self) -> Any:
        ...
    


class Paginator:
    PAGE_ITERATOR_CLS: Any = ...
    def __init__(self, method: Any, pagination_config: Any, model: Any) -> None:
        ...
    
    @property
    def result_keys(self) -> Any:
        ...
    
    def paginate(self, **kwargs: Any) -> Any:
        ...
    


class ResultKeyIterator:
    result_key: Any = ...
    def __init__(self, pages_iterator: Any, result_key: Any) -> None:
        ...
    
    def __iter__(self) -> Any:
        ...
    


