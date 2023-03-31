"""
This type stub file was generated by pyright.
"""

from functools import total_ordering

class cached_property:
    """
    Decorator that converts a method with a single self argument into a
    property cached on the instance.

    A cached property can be made out of an existing method:
    (e.g. ``url = cached_property(get_absolute_url)``).
    """
    name = ...
    @staticmethod
    def func(instance):
        ...
    
    def __init__(self, func, name=...) -> None:
        ...
    
    def __set_name__(self, owner, name): # -> None:
        ...
    
    def __get__(self, instance, cls=...): # -> Self@cached_property:
        """
        Call the function and put the return value in instance.__dict__ so that
        subsequent attribute access on the instance returns the cached value
        instead of calling cached_property.__get__().
        """
        ...
    


class classproperty:
    """
    Decorator that converts a method with a single cls argument into a property
    that can be accessed directly from the class.
    """
    def __init__(self, method=...) -> None:
        ...
    
    def __get__(self, instance, cls=...):
        ...
    
    def getter(self, method): # -> Self@classproperty:
        ...
    


class Promise:
    """
    Base class for the proxy class created in the closure of the lazy function.
    It's used to recognize promises in code.
    """
    ...


def lazy(func, *resultclasses): # -> _Wrapped[(...), Unknown, (*args: Unknown, **kw: Unknown), __proxy__]:
    """
    Turn any callable into a lazy evaluated callable. result classes or types
    is required -- at least one is needed so that the automatic forcing of
    the lazy evaluation code is triggered. Results are not memoized; the
    function is evaluated on every access.
    """
    @total_ordering
    class __proxy__(Promise):
        """
        Encapsulate a function call and act as a proxy for methods that are
        called on the result of that function. The function is not evaluated
        until one of the methods on the result is called.
        """
        ...
    
    

def lazystr(text): # -> __proxy__:
    """
    Shortcut for the common case of a lazy callable that returns str.
    """
    ...

def keep_lazy(*resultclasses): # -> (func: Unknown) -> _Wrapped[(...), Unknown, (*args: Unknown, **kwargs: Unknown), __proxy__ | Unknown]:
    """
    A decorator that allows a function to be called with one or more lazy
    arguments. If none of the args are lazy, the function is evaluated
    immediately, otherwise a __proxy__ is returned that will evaluate the
    function when needed.
    """
    ...

def keep_lazy_text(func): # -> _Wrapped[(...), Unknown, (*args: Unknown, **kwargs: Unknown), __proxy__ | Unknown]:
    """
    A decorator for functions that accept lazy arguments and return text.
    """
    ...

empty = ...
def new_method_proxy(func): # -> (self: Unknown, *args: Unknown) -> Unknown:
    ...

class LazyObject:
    """
    A wrapper for another class that can be used to delay instantiation of the
    wrapped class.

    By subclassing, you have the opportunity to intercept and alter the
    instantiation. If you don't need to do that, use SimpleLazyObject.
    """
    _wrapped = ...
    def __init__(self) -> None:
        ...
    
    def __getattribute__(self, name): # -> Any:
        ...
    
    __getattr__ = ...
    def __setattr__(self, name, value): # -> None:
        ...
    
    def __delattr__(self, name): # -> None:
        ...
    
    def __reduce__(self): # -> tuple[(wrapped: Unknown) -> Unknown, tuple[object | None]]:
        ...
    
    def __copy__(self): # -> Self@LazyObject | object | None:
        ...
    
    def __deepcopy__(self, memo): # -> Self@LazyObject | object | None:
        ...
    
    __bytes__ = ...
    __str__ = ...
    __bool__ = ...
    __dir__ = ...
    __class__ = ...
    __eq__ = ...
    __lt__ = ...
    __gt__ = ...
    __ne__ = ...
    __hash__ = ...
    __getitem__ = ...
    __setitem__ = ...
    __delitem__ = ...
    __iter__ = ...
    __len__ = ...
    __contains__ = ...


def unpickle_lazyobject(wrapped):
    """
    Used to unpickle lazy objects. Just return its argument, which will be the
    wrapped object.
    """
    ...

class SimpleLazyObject(LazyObject):
    """
    A lazy object initialized from any function.

    Designed for compound objects of unknown type. For builtins or objects of
    known type, use django.utils.functional.lazy.
    """
    def __init__(self, func) -> None:
        """
        Pass in a callable that returns the object to be wrapped.

        If copies are made of the resulting SimpleLazyObject, which can happen
        in various circumstances within Django, then you must ensure that the
        callable can be safely run more than once and will return the same
        value.
        """
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __copy__(self): # -> SimpleLazyObject | Any:
        ...
    
    def __deepcopy__(self, memo): # -> SimpleLazyObject | Any:
        ...
    
    __add__ = ...
    @new_method_proxy
    def __radd__(self, other):
        ...
    


def partition(predicate, values): # -> tuple[list[Unknown], list[Unknown]]:
    """
    Split the values into two sets, based on the return value of the function
    (True/False). e.g.:

        >>> partition(lambda x: x > 3, range(5))
        [0, 1, 2, 3], [4]
    """
    ...

