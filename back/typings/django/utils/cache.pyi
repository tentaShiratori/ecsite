"""
This type stub file was generated by pyright.
"""

"""
This module contains helper functions for controlling caching. It does so by
managing the "Vary" header of responses. It includes functions to patch the
header of response objects directly and decorators that change functions to do
that header-patching themselves.

For information on the Vary header, see:

    https://tools.ietf.org/html/rfc7231#section-7.1.4

Essentially, the "Vary" HTTP header defines which headers a cache should take
into account when building its cache key. Requests with the same path but
different header content for headers named in "Vary" need to get different
cache keys to prevent delivery of wrong content.

An example: i18n middleware would need to distinguish caches by the
"Accept-language" header.
"""
cc_delim_re = ...
def patch_cache_control(response, **kwargs): # -> None:
    """
    Patch the Cache-Control header by adding all keyword arguments to it.
    The transformation is as follows:

    * All keyword parameter names are turned to lowercase, and underscores
      are converted to hyphens.
    * If the value of a parameter is True (exactly True, not just a
      true value), only the parameter name is added to the header.
    * All other parameters are added with their value, after applying
      str() to it.
    """
    ...

def get_max_age(response): # -> int | None:
    """
    Return the max-age from the response Cache-Control header as an integer,
    or None if it wasn't found or wasn't an integer.
    """
    ...

def set_response_etag(response):
    ...

def get_conditional_response(request, etag=..., last_modified=..., response=...): # -> HttpResponse | HttpResponseNotModified | None:
    ...

def patch_response_headers(response, cache_timeout=...): # -> None:
    """
    Add HTTP caching headers to the given HttpResponse: Expires and
    Cache-Control.

    Each header is only added if it isn't already set.

    cache_timeout is in seconds. The CACHE_MIDDLEWARE_SECONDS setting is used
    by default.
    """
    ...

def add_never_cache_headers(response): # -> None:
    """
    Add headers to a response to indicate that a page should never be cached.
    """
    ...

def patch_vary_headers(response, newheaders): # -> None:
    """
    Add (or update) the "Vary" header in the given HttpResponse object.
    newheaders is a list of header names that should be in "Vary". If headers
    contains an asterisk, then "Vary" header will consist of a single asterisk
    '*'. Otherwise, existing headers in "Vary" aren't removed.
    """
    ...

def has_vary_header(response, header_query): # -> bool:
    """
    Check to see if the response has a given header name in its Vary header.
    """
    ...

def get_cache_key(request, key_prefix=..., method=..., cache=...): # -> Any | str | None:
    """
    Return a cache key based on the request URL and query. It can be used
    in the request phase because it pulls the list of headers to take into
    account from the global URL registry and uses those to build a cache key
    to check against.

    If there isn't a headerlist stored, return None, indicating that the page
    needs to be rebuilt.
    """
    ...

def learn_cache_key(request, response, cache_timeout=..., key_prefix=..., cache=...): # -> Any | str:
    """
    Learn what headers to take into account for some request URL from the
    response object. Store those headers in a global URL registry so that
    later access to that URL will know what headers to take into account
    without building the response object itself. The headers are named in the
    Vary header of the response, but we want to prevent response generation.

    The list of headers to use for cache key generation is stored in the same
    cache as the pages themselves. If the cache ages some data out of the
    cache, this just means that we have to build the response once to get at
    the Vary header and so at the list of headers to use for the cache key.
    """
    ...

