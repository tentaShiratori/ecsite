"""
This type stub file was generated by pyright.
"""

from collections.abc import Mapping

class OrderedSet:
    """
    A set which keeps the ordering of the inserted items.
    """
    def __init__(self, iterable=...) -> None:
        ...
    
    def add(self, item): # -> None:
        ...
    
    def remove(self, item): # -> None:
        ...
    
    def discard(self, item): # -> None:
        ...
    
    def __iter__(self): # -> Iterator[Any]:
        ...
    
    def __reversed__(self): # -> reversed[Any]:
        ...
    
    def __contains__(self, item): # -> bool:
        ...
    
    def __bool__(self): # -> bool:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __repr__(self): # -> str:
        ...
    


class MultiValueDictKeyError(KeyError):
    ...


class MultiValueDict(dict):
    """
    A subclass of dictionary customized to handle multiple values for the
    same key.

    >>> d = MultiValueDict({'name': ['Adrian', 'Simon'], 'position': ['Developer']})
    >>> d['name']
    'Simon'
    >>> d.getlist('name')
    ['Adrian', 'Simon']
    >>> d.getlist('doesnotexist')
    []
    >>> d.getlist('doesnotexist', ['Adrian', 'Simon'])
    ['Adrian', 'Simon']
    >>> d.get('lastname', 'nonexistent')
    'nonexistent'
    >>> d.setlist('lastname', ['Holovaty', 'Willison'])

    This class exists to solve the irritating problem raised by cgi.parse_qs,
    which returns a list for every key, even though most web forms submit
    single name-value pairs.
    """
    def __init__(self, key_to_list_mapping=...) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __getitem__(self, key): # -> list[Unknown]:
        """
        Return the last data value for this key, or [] if it's an empty list;
        raise KeyError if not found.
        """
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def __copy__(self): # -> MultiValueDict:
        ...
    
    def __deepcopy__(self, memo): # -> MultiValueDict:
        ...
    
    def __getstate__(self): # -> dict[str, Unknown]:
        ...
    
    def __setstate__(self, obj_dict): # -> None:
        ...
    
    def get(self, key, default=...): # -> list[Unknown] | None:
        """
        Return the last data value for the passed key. If key doesn't exist
        or value is an empty list, return `default`.
        """
        ...
    
    def getlist(self, key, default=...): # -> list[Unknown] | None:
        """
        Return the list of values for the key. If key doesn't exist, return a
        default value.
        """
        ...
    
    def setlist(self, key, list_): # -> None:
        ...
    
    def setdefault(self, key, default=...): # -> list[Unknown]:
        ...
    
    def setlistdefault(self, key, default_list=...): # -> list[Unknown] | None:
        ...
    
    def appendlist(self, key, value): # -> None:
        """Append an item to the internal list associated with key."""
        ...
    
    def items(self): # -> Generator[tuple[Unknown, Unknown | list[Unknown]], None, None]:
        """
        Yield (key, value) pairs, where value is the last item in the list
        associated with the key.
        """
        ...
    
    def lists(self): # -> Iterator[tuple[Unknown, Unknown]]:
        """Yield (key, list) pairs."""
        ...
    
    def values(self): # -> Generator[Unknown | list[Unknown], None, None]:
        """Yield the last value on every key list."""
        ...
    
    def copy(self): # -> Self@MultiValueDict:
        """Return a shallow copy of this object."""
        ...
    
    def update(self, *args, **kwargs): # -> None:
        """Extend rather than replace existing key lists."""
        ...
    
    def dict(self): # -> dict[Unknown, Unknown | list[Unknown]]:
        """Return current object as a dict with singular values."""
        ...
    


class ImmutableList(tuple):
    """
    A tuple-like object that raises useful errors when it is asked to mutate.

    Example::

        >>> a = ImmutableList(range(5), warning="You cannot mutate this.")
        >>> a[3] = '4'
        Traceback (most recent call last):
            ...
        AttributeError: You cannot mutate this.
    """
    def __new__(cls, *args, warning=..., **kwargs): # -> Self@ImmutableList:
        ...
    
    def complain(self, *args, **kwargs):
        ...
    
    __delitem__ = ...
    __delslice__ = ...
    __iadd__ = ...
    __imul__ = ...
    __setitem__ = ...
    __setslice__ = ...
    append = ...
    extend = ...
    insert = ...
    pop = ...
    remove = ...
    sort = ...
    reverse = ...


class DictWrapper(dict):
    """
    Wrap accesses to a dictionary so that certain values (those starting with
    the specified prefix) are passed through a function before being returned.
    The prefix is removed before looking up the real value.

    Used by the SQL construction code to ensure that values are correctly
    quoted before being used.
    """
    def __init__(self, data, func, prefix) -> None:
        ...
    
    def __getitem__(self, key):
        """
        Retrieve the real value after stripping the prefix string (if
        present). If the prefix is present, pass the value through self.func
        before returning, otherwise return the raw value.
        """
        ...
    


class CaseInsensitiveMapping(Mapping):
    """
    Mapping allowing case-insensitive key lookups. Original case of keys is
    preserved for iteration and string representation.

    Example::

        >>> ci_map = CaseInsensitiveMapping({'name': 'Jane'})
        >>> ci_map['Name']
        Jane
        >>> ci_map['NAME']
        Jane
        >>> ci_map['name']
        Jane
        >>> ci_map  # original case preserved
        {'name': 'Jane'}
    """
    def __init__(self, data) -> None:
        ...
    
    def __getitem__(self, key):
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __iter__(self): # -> Generator[Unknown, None, None]:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def copy(self): # -> Self@CaseInsensitiveMapping:
        ...
    


