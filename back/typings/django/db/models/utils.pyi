"""
This type stub file was generated by pyright.
"""

import functools

def make_model_tuple(model): # -> tuple[Unknown, ...] | tuple[str, str] | tuple[Unknown, Unknown]:
    """
    Take a model or a string of the form "app_label.ModelName" and return a
    corresponding ("app_label", "modelname") tuple. If a tuple is passed in,
    assume it's a valid model tuple already and return it unchanged.
    """
    ...

def resolve_callables(mapping): # -> Generator[tuple[Unknown, Unknown], None, None]:
    """
    Generate key/value pairs for the given mapping where the values are
    evaluated if they're callable.
    """
    ...

def unpickle_named_row(names, values): # -> Self@Row:
    ...

@functools.lru_cache
def create_namedtuple_class(*names): # -> Type[Row]:
    ...

