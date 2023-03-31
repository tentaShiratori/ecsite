"""
This type stub file was generated by pyright.
"""

"""
Global Django exception and warning classes.
"""
class FieldDoesNotExist(Exception):
    """The requested model field does not exist"""
    ...


class AppRegistryNotReady(Exception):
    """The django.apps registry is not populated yet"""
    ...


class ObjectDoesNotExist(Exception):
    """The requested object does not exist"""
    silent_variable_failure = ...


class MultipleObjectsReturned(Exception):
    """The query returned multiple objects when only one was expected."""
    ...


class SuspiciousOperation(Exception):
    """The user did something suspicious"""
    ...


class SuspiciousMultipartForm(SuspiciousOperation):
    """Suspect MIME request in multipart form data"""
    ...


class SuspiciousFileOperation(SuspiciousOperation):
    """A Suspicious filesystem operation was attempted"""
    ...


class DisallowedHost(SuspiciousOperation):
    """HTTP_HOST header contains invalid value"""
    ...


class DisallowedRedirect(SuspiciousOperation):
    """Redirect to scheme not in allowed list"""
    ...


class TooManyFieldsSent(SuspiciousOperation):
    """
    The number of fields in a GET or POST request exceeded
    settings.DATA_UPLOAD_MAX_NUMBER_FIELDS.
    """
    ...


class TooManyFilesSent(SuspiciousOperation):
    """
    The number of fields in a GET or POST request exceeded
    settings.DATA_UPLOAD_MAX_NUMBER_FILES.
    """
    ...


class RequestDataTooBig(SuspiciousOperation):
    """
    The size of the request (excluding any file uploads) exceeded
    settings.DATA_UPLOAD_MAX_MEMORY_SIZE.
    """
    ...


class RequestAborted(Exception):
    """The request was closed before it was completed, or timed out."""
    ...


class BadRequest(Exception):
    """The request is malformed and cannot be processed."""
    ...


class PermissionDenied(Exception):
    """The user did not have permission to do that"""
    ...


class ViewDoesNotExist(Exception):
    """The requested view does not exist"""
    ...


class MiddlewareNotUsed(Exception):
    """This middleware is not used in this server configuration"""
    ...


class ImproperlyConfigured(Exception):
    """Django is somehow improperly configured"""
    ...


class FieldError(Exception):
    """Some kind of problem with a model field."""
    ...


NON_FIELD_ERRORS = ...
class ValidationError(Exception):
    """An error while validating data."""
    def __init__(self, message, code=..., params=...) -> None:
        """
        The `message` argument can be a single error, a list of errors, or a
        dictionary that maps field names to lists of errors. What we define as
        an "error" can be either a simple string or an instance of
        ValidationError with its message attribute set, and what we define as
        list or dictionary can be an actual `list` or `dict` or an instance
        of ValidationError with its `error_list` or `error_dict` attribute set.
        """
        ...
    
    @property
    def message_dict(self): # -> dict[Unknown, Unknown]:
        ...
    
    @property
    def messages(self): # -> list[Unknown] | list[tuple[Unknown, list[Unknown]] | str]:
        ...
    
    def update_error_dict(self, error_dict):
        ...
    
    def __iter__(self): # -> Generator[tuple[Unknown, list[Unknown]] | str, None, None]:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


class EmptyResultSet(Exception):
    """A database query predicate is impossible."""
    ...


class SynchronousOnlyOperation(Exception):
    """The user tried to call a sync-only function from an async context."""
    ...


