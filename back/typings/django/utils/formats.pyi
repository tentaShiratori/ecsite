"""
This type stub file was generated by pyright.
"""

import functools

_format_cache = ...
_format_modules_cache = ...
ISO_INPUT_FORMATS = ...
FORMAT_SETTINGS = ...
def reset_format_cache(): # -> None:
    """Clear any cached formats.

    This method is provided primarily for testing purposes,
    so that the effects of cached formats can be removed.
    """
    ...

def iter_format_modules(lang, format_module_path=...): # -> Generator[ModuleType, None, None]:
    """Find format modules."""
    ...

def get_format_modules(lang=...):
    """Return a list of the format modules found."""
    ...

def get_format(format_type, lang=..., use_l10n=...): # -> str | Any | list[Any]:
    """
    For a specific format type, return the format for the current
    language (locale). Default to the format in the settings.
    format_type is the name of the format, e.g. 'DATE_FORMAT'.

    If use_l10n is provided and is not None, it forces the value to
    be localized (or not), overriding the value of settings.USE_L10N.
    """
    ...

get_format_lazy = ...
def date_format(value, format=..., use_l10n=...): # -> LiteralString:
    """
    Format a datetime.date or datetime.datetime object using a
    localizable format.

    If use_l10n is provided and is not None, that will force the value to
    be localized (or not), overriding the value of settings.USE_L10N.
    """
    ...

def time_format(value, format=..., use_l10n=...): # -> LiteralString:
    """
    Format a datetime.time object using a localizable format.

    If use_l10n is provided and is not None, it forces the value to
    be localized (or not), overriding the value of settings.USE_L10N.
    """
    ...

def number_format(value, decimal_pos=..., use_l10n=..., force_grouping=...):
    """
    Format a numeric value using localization settings.

    If use_l10n is provided and is not None, it forces the value to
    be localized (or not), overriding the value of settings.USE_L10N.
    """
    ...

def localize(value, use_l10n=...): # -> str | LiteralString:
    """
    Check if value is a localizable type (date, number...) and return it
    formatted as a string using current locale format.

    If use_l10n is provided and is not None, it forces the value to
    be localized (or not), overriding the value of settings.USE_L10N.
    """
    ...

def localize_input(value, default=...): # -> str:
    """
    Check if an input value is a localizable type and return it
    formatted with the appropriate formatting string of the current locale.
    """
    ...

@functools.lru_cache
def sanitize_strftime_format(fmt): # -> str:
    """
    Ensure that certain specifiers are correctly padded with leading zeros.

    For years < 1000 specifiers %C, %F, %G, and %Y don't work as expected for
    strftime provided by glibc on Linux as they don't pad the year or century
    with leading zeros. Support for specifying the padding explicitly is
    available, however, which can be used to fix this issue.

    FreeBSD, macOS, and Windows do not support explicitly specifying the
    padding, but return four digit years (with leading zeros) as expected.

    This function checks whether the %Y produces a correctly padded string and,
    if not, makes the following substitutions:

    - %C → %02C
    - %F → %010F
    - %G → %04G
    - %Y → %04Y

    See https://bugs.python.org/issue13305 for more details.
    """
    ...

def sanitize_separators(value): # -> LiteralString:
    """
    Sanitize a value according to the current decimal and
    thousand separator setting. Used with form field input.
    """
    ...

