"""
This type stub file was generated by pyright.
"""

import functools
from contextlib import ContextDecorator

"""
Timezone-related classes and functions.
"""
__all__ = ["utc", "get_fixed_timezone", "get_default_timezone", "get_default_timezone_name", "get_current_timezone", "get_current_timezone_name", "activate", "deactivate", "override", "localtime", "localdate", "now", "is_aware", "is_naive", "make_aware", "make_naive"]
NOT_PASSED = ...
def __getattr__(name): # -> timezone:
    ...

def get_fixed_timezone(offset): # -> timezone:
    """Return a tzinfo instance with a fixed offset from UTC."""
    ...

@functools.lru_cache
def get_default_timezone(): # -> _UTCclass | StaticTzInfo | DstTzInfo | ZoneInfo:
    """
    Return the default time zone as a tzinfo instance.

    This is the time zone defined by settings.TIME_ZONE.
    """
    ...

def get_default_timezone_name(): # -> str:
    """Return the name of the default time zone."""
    ...

_active = ...
def get_current_timezone(): # -> Any | _UTCclass | StaticTzInfo | DstTzInfo | ZoneInfo:
    """Return the currently active time zone as a tzinfo instance."""
    ...

def get_current_timezone_name(): # -> Any | str:
    """Return the name of the currently active time zone."""
    ...

def activate(timezone): # -> None:
    """
    Set the time zone for the current thread.

    The ``timezone`` argument must be an instance of a tzinfo subclass or a
    time zone name.
    """
    ...

def deactivate(): # -> None:
    """
    Unset the time zone for the current thread.

    Django will then use the time zone defined by settings.TIME_ZONE.
    """
    ...

class override(ContextDecorator):
    """
    Temporarily set the time zone for the current thread.

    This is a context manager that uses django.utils.timezone.activate()
    to set the timezone on entry and restores the previously active timezone
    on exit.

    The ``timezone`` argument must be an instance of a ``tzinfo`` subclass, a
    time zone name, or ``None``. If it is ``None``, Django enables the default
    time zone.
    """
    def __init__(self, timezone) -> None:
        ...
    
    def __enter__(self): # -> None:
        ...
    
    def __exit__(self, exc_type, exc_value, traceback): # -> None:
        ...
    


def template_localtime(value, use_tz=...): # -> datetime:
    """
    Check if value is a datetime and converts it to local time if necessary.

    If use_tz is provided and is not None, that will force the value to
    be converted (or not), overriding the value of settings.USE_TZ.

    This function is designed for use by the template engine.
    """
    ...

def localtime(value=..., timezone=...): # -> datetime:
    """
    Convert an aware datetime.datetime to local time.

    Only aware datetimes are allowed. When value is omitted, it defaults to
    now().

    Local time is defined by the current time zone, unless another time zone
    is specified.
    """
    ...

def localdate(value=..., timezone=...): # -> _Date:
    """
    Convert an aware datetime to local time and return the value's date.

    Only aware datetimes are allowed. When value is omitted, it defaults to
    now().

    Local time is defined by the current time zone, unless another time zone is
    specified.
    """
    ...

def now(): # -> datetime:
    """
    Return an aware or naive datetime.datetime, depending on settings.USE_TZ.
    """
    ...

def is_aware(value): # -> bool:
    """
    Determine if a given datetime.datetime is aware.

    The concept is defined in Python's docs:
    https://docs.python.org/library/datetime.html#datetime.tzinfo

    Assuming value.tzinfo is either None or a proper datetime.tzinfo,
    value.utcoffset() implements the appropriate logic.
    """
    ...

def is_naive(value): # -> bool:
    """
    Determine if a given datetime.datetime is naive.

    The concept is defined in Python's docs:
    https://docs.python.org/library/datetime.html#datetime.tzinfo

    Assuming value.tzinfo is either None or a proper datetime.tzinfo,
    value.utcoffset() implements the appropriate logic.
    """
    ...

def make_aware(value, timezone=..., is_dst=...): # -> Any | datetime:
    """Make a naive datetime.datetime in a given time zone aware."""
    ...

def make_naive(value, timezone=...):
    """Make an aware datetime.datetime naive in a given time zone."""
    ...

_PYTZ_IMPORTED = ...
_DIR = ...
def __dir__(): # -> list[str]:
    ...

