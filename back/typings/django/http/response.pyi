"""
This type stub file was generated by pyright.
"""

from django.utils.datastructures import CaseInsensitiveMapping

_charset_from_content_type_re = ...
class ResponseHeaders(CaseInsensitiveMapping):
    def __init__(self, data) -> None:
        """
        Populate the initial data using __setitem__ to ensure values are
        correctly encoded.
        """
        ...
    
    def __delitem__(self, key): # -> None:
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def pop(self, key, default=...): # -> None:
        ...
    
    def setdefault(self, key, value): # -> None:
        ...
    


class BadHeaderError(ValueError):
    ...


class HttpResponseBase:
    """
    An HTTP response base class with dictionary-accessed headers.

    This class doesn't handle content. It should not be used directly.
    Use the HttpResponse and StreamingHttpResponse subclasses instead.
    """
    status_code = ...
    def __init__(self, content_type=..., status=..., reason=..., charset=..., headers=...) -> None:
        ...
    
    @property
    def reason_phrase(self): # -> str:
        ...
    
    @reason_phrase.setter
    def reason_phrase(self, value): # -> None:
        ...
    
    @property
    def charset(self): # -> Any:
        ...
    
    @charset.setter
    def charset(self, value): # -> None:
        ...
    
    def serialize_headers(self): # -> bytes:
        """HTTP headers as a bytestring."""
        ...
    
    __bytes__ = ...
    def __setitem__(self, header, value): # -> None:
        ...
    
    def __delitem__(self, header): # -> None:
        ...
    
    def __getitem__(self, header):
        ...
    
    def has_header(self, header): # -> bool:
        """Case-insensitive check for a header."""
        ...
    
    __contains__ = ...
    def items(self): # -> ItemsView[Unknown, Unknown]:
        ...
    
    def get(self, header, alternate=...): # -> None:
        ...
    
    def set_cookie(self, key, value=..., max_age=..., expires=..., path=..., domain=..., secure=..., httponly=..., samesite=...): # -> None:
        """
        Set a cookie.

        ``expires`` can be:
        - a string in the correct format,
        - a naive ``datetime.datetime`` object in UTC,
        - an aware ``datetime.datetime`` object in any time zone.
        If it is a ``datetime.datetime`` object then calculate ``max_age``.

        ``max_age`` can be:
        - int/float specifying seconds,
        - ``datetime.timedelta`` object.
        """
        ...
    
    def setdefault(self, key, value): # -> None:
        """Set a header unless it has already been set."""
        ...
    
    def set_signed_cookie(self, key, value, salt=..., **kwargs): # -> None:
        ...
    
    def delete_cookie(self, key, path=..., domain=..., samesite=...): # -> None:
        ...
    
    def make_bytes(self, value): # -> bytes:
        """Turn a value into a bytestring encoded in the output charset."""
        ...
    
    def close(self): # -> None:
        ...
    
    def write(self, content):
        ...
    
    def flush(self): # -> None:
        ...
    
    def tell(self):
        ...
    
    def readable(self): # -> Literal[False]:
        ...
    
    def seekable(self): # -> Literal[False]:
        ...
    
    def writable(self): # -> Literal[False]:
        ...
    
    def writelines(self, lines):
        ...
    


class HttpResponse(HttpResponseBase):
    """
    An HTTP response class with a string as content.

    This content can be read, appended to, or replaced.
    """
    streaming = ...
    def __init__(self, content=..., *args, **kwargs) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def serialize(self): # -> bytes:
        """Full HTTP message, including headers, as a bytestring."""
        ...
    
    __bytes__ = ...
    @property
    def content(self): # -> bytes:
        ...
    
    @content.setter
    def content(self, value): # -> None:
        ...
    
    def __iter__(self): # -> Iterator[bytes]:
        ...
    
    def write(self, content): # -> None:
        ...
    
    def tell(self): # -> int:
        ...
    
    def getvalue(self): # -> bytes:
        ...
    
    def writable(self): # -> Literal[True]:
        ...
    
    def writelines(self, lines): # -> None:
        ...
    


class StreamingHttpResponse(HttpResponseBase):
    """
    A streaming HTTP response class with an iterator as content.

    This should only be iterated once, when the response is streamed to the
    client. However, it can be appended to or replaced with a new iterator
    that wraps the original content (or yields entirely new content).
    """
    streaming = ...
    def __init__(self, streaming_content=..., *args, **kwargs) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    @property
    def content(self):
        ...
    
    @property
    def streaming_content(self): # -> map[bytes]:
        ...
    
    @streaming_content.setter
    def streaming_content(self, value): # -> None:
        ...
    
    def __iter__(self): # -> map[bytes]:
        ...
    
    def getvalue(self): # -> bytes:
        ...
    


class FileResponse(StreamingHttpResponse):
    """
    A streaming HTTP response class optimized for files.
    """
    block_size = ...
    def __init__(self, *args, as_attachment=..., filename=..., **kwargs) -> None:
        ...
    
    def set_headers(self, filelike): # -> None:
        """
        Set some common response headers (Content-Length, Content-Type, and
        Content-Disposition) based on the `filelike` response content.
        """
        ...
    


class HttpResponseRedirectBase(HttpResponse):
    allowed_schemes = ...
    def __init__(self, redirect_to, *args, **kwargs) -> None:
        ...
    
    url = ...
    def __repr__(self): # -> str:
        ...
    


class HttpResponseRedirect(HttpResponseRedirectBase):
    status_code = ...


class HttpResponsePermanentRedirect(HttpResponseRedirectBase):
    status_code = ...


class HttpResponseNotModified(HttpResponse):
    status_code = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @HttpResponse.content.setter
    def content(self, value): # -> None:
        ...
    


class HttpResponseBadRequest(HttpResponse):
    status_code = ...


class HttpResponseNotFound(HttpResponse):
    status_code = ...


class HttpResponseForbidden(HttpResponse):
    status_code = ...


class HttpResponseNotAllowed(HttpResponse):
    status_code = ...
    def __init__(self, permitted_methods, *args, **kwargs) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    


class HttpResponseGone(HttpResponse):
    status_code = ...


class HttpResponseServerError(HttpResponse):
    status_code = ...


class Http404(Exception):
    ...


class JsonResponse(HttpResponse):
    """
    An HTTP response class that consumes data to be serialized to JSON.

    :param data: Data to be dumped into json. By default only ``dict`` objects
      are allowed to be passed due to a security flaw before ECMAScript 5. See
      the ``safe`` parameter for more information.
    :param encoder: Should be a json encoder class. Defaults to
      ``django.core.serializers.json.DjangoJSONEncoder``.
    :param safe: Controls if only ``dict`` objects may be serialized. Defaults
      to ``True``.
    :param json_dumps_params: A dictionary of kwargs passed to json.dumps().
    """
    def __init__(self, data, encoder=..., safe=..., json_dumps_params=..., **kwargs) -> None:
        ...
    

