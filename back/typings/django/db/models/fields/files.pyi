"""
This type stub file was generated by pyright.
"""

from django.core.files.base import File
from django.core.files.images import ImageFile
from django.db.models.fields import Field
from django.db.models.query_utils import DeferredAttribute

class FieldFile(File):
    def __init__(self, instance, field, name) -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    file = ...
    @property
    def path(self):
        ...
    
    @property
    def url(self):
        ...
    
    @property
    def size(self): # -> Any:
        ...
    
    def open(self, mode=...): # -> Self@FieldFile:
        ...
    
    def save(self, name, content, save=...): # -> None:
        ...
    
    def delete(self, save=...): # -> None:
        ...
    
    @property
    def closed(self): # -> Any | Literal[True]:
        ...
    
    def close(self): # -> None:
        ...
    
    def __getstate__(self): # -> dict[str, Unknown]:
        ...
    
    def __setstate__(self, state): # -> None:
        ...
    


class FileDescriptor(DeferredAttribute):
    """
    The descriptor for the file attribute on the model instance. Return a
    FieldFile when accessed so you can write code like::

        >>> from myapp.models import MyModel
        >>> instance = MyModel.objects.get(pk=1)
        >>> instance.file.size

    Assign a file object on assignment so you can do::

        >>> with open('/path/to/hello.world') as f:
        ...     instance.file = File(f)
    """
    def __get__(self, instance, cls=...): # -> Self@FileDescriptor:
        ...
    
    def __set__(self, instance, value): # -> None:
        ...
    


class FileField(Field):
    attr_class = FieldFile
    descriptor_class = FileDescriptor
    description = ...
    def __init__(self, verbose_name=..., name=..., upload_to=..., storage=..., **kwargs) -> None:
        ...
    
    def check(self, **kwargs): # -> list[Unknown]:
        ...
    
    def deconstruct(self): # -> tuple[Unknown | None, str, list[Unknown], dict[Unknown, Unknown]]:
        ...
    
    def get_internal_type(self): # -> Literal['FileField']:
        ...
    
    def get_prep_value(self, value): # -> str | None:
        ...
    
    def pre_save(self, model_instance, add): # -> Any:
        ...
    
    def contribute_to_class(self, cls, name, **kwargs): # -> None:
        ...
    
    def generate_filename(self, instance, filename): # -> Any:
        """
        Apply (if callable) or prepend (if a string) upload_to to the filename,
        then delegate further processing of the name to the storage backend.
        Until the storage layer, all file paths are expected to be Unix style
        (with forward slashes).
        """
        ...
    
    def save_form_data(self, instance, data): # -> None:
        ...
    
    def formfield(self, **kwargs): # -> CharField | TypedChoiceField:
        ...
    


class ImageFileDescriptor(FileDescriptor):
    """
    Just like the FileDescriptor, but for ImageFields. The only difference is
    assigning the width/height to the width_field/height_field, if appropriate.
    """
    def __set__(self, instance, value): # -> None:
        ...
    


class ImageFieldFile(ImageFile, FieldFile):
    def delete(self, save=...): # -> None:
        ...
    


class ImageField(FileField):
    attr_class = ImageFieldFile
    descriptor_class = ImageFileDescriptor
    description = ...
    def __init__(self, verbose_name=..., name=..., width_field=..., height_field=..., **kwargs) -> None:
        ...
    
    def check(self, **kwargs): # -> list[Unknown]:
        ...
    
    def deconstruct(self): # -> tuple[Unknown | None, str, list[Unknown], dict[Unknown, Unknown]]:
        ...
    
    def contribute_to_class(self, cls, name, **kwargs): # -> None:
        ...
    
    def update_dimension_fields(self, instance, force=..., *args, **kwargs): # -> None:
        """
        Update field's width and height fields, if defined.

        This method is hooked up to model's post_init signal to update
        dimensions after instantiating a model instance.  However, dimensions
        won't be updated if the dimensions fields are already populated.  This
        avoids unnecessary recalculation when loading an object from the
        database.

        Dimensions can be forced to update with force=True, which is how
        ImageFileDescriptor.__set__ calls this method.
        """
        ...
    
    def formfield(self, **kwargs): # -> CharField | TypedChoiceField:
        ...
    

