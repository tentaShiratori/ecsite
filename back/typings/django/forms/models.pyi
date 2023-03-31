"""
This type stub file was generated by pyright.
"""

from django.forms.fields import ChoiceField, Field
from django.forms.forms import BaseForm, DeclarativeFieldsMetaclass
from django.forms.formsets import BaseFormSet
from django.forms.widgets import HiddenInput, MultipleHiddenInput, SelectMultiple

"""
Helper functions for creating Form classes from Django models
and database field objects.
"""
__all__ = ("ModelForm", "BaseModelForm", "model_to_dict", "fields_for_model", "ModelChoiceField", "ModelMultipleChoiceField", "ALL_FIELDS", "BaseModelFormSet", "modelformset_factory", "BaseInlineFormSet", "inlineformset_factory", "modelform_factory")
ALL_FIELDS = ...
def construct_instance(form, instance, fields=..., exclude=...):
    """
    Construct and return a model instance from the bound ``form``'s
    ``cleaned_data``, but do not save the returned instance to the database.
    """
    ...

def model_to_dict(instance, fields=..., exclude=...): # -> dict[Unknown, Unknown]:
    """
    Return a dict containing the data in ``instance`` suitable for passing as
    a Form's ``initial`` keyword argument.

    ``fields`` is an optional list of field names. If provided, return only the
    named.

    ``exclude`` is an optional list of field names. If provided, exclude the
    named from the returned dict, even if they are listed in the ``fields``
    argument.
    """
    ...

def apply_limit_choices_to_to_formfield(formfield): # -> None:
    """Apply limit_choices_to to the formfield's queryset if needed."""
    ...

def fields_for_model(model, fields=..., exclude=..., widgets=..., formfield_callback=..., localized_fields=..., labels=..., help_texts=..., error_messages=..., field_classes=..., *, apply_limit_choices_to=...):
    """
    Return a dictionary containing form fields for the given model.

    ``fields`` is an optional list of field names. If provided, return only the
    named fields.

    ``exclude`` is an optional list of field names. If provided, exclude the
    named fields from the returned fields, even if they are listed in the
    ``fields`` argument.

    ``widgets`` is a dictionary of model field names mapped to a widget.

    ``formfield_callback`` is a callable that takes a model field and returns
    a form field.

    ``localized_fields`` is a list of names of fields which should be localized.

    ``labels`` is a dictionary of model field names mapped to a label.

    ``help_texts`` is a dictionary of model field names mapped to a help text.

    ``error_messages`` is a dictionary of model field names mapped to a
    dictionary of error messages.

    ``field_classes`` is a dictionary of model field names mapped to a form
    field class.

    ``apply_limit_choices_to`` is a boolean indicating if limit_choices_to
    should be applied to a field's queryset.
    """
    ...

class ModelFormOptions:
    def __init__(self, options=...) -> None:
        ...
    


class ModelFormMetaclass(DeclarativeFieldsMetaclass):
    def __new__(mcs, name, bases, attrs): # -> Self@ModelFormMetaclass:
        ...
    


class BaseModelForm(BaseForm):
    def __init__(self, data=..., files=..., auto_id=..., prefix=..., initial=..., error_class=..., label_suffix=..., empty_permitted=..., instance=..., use_required_attribute=..., renderer=...) -> None:
        ...
    
    def clean(self): # -> dict[Unknown, Unknown]:
        ...
    
    def validate_unique(self): # -> None:
        """
        Call the instance's validate_unique() method and update the form's
        validation errors if any were raised.
        """
        ...
    
    def save(self, commit=...):
        """
        Save this form's self.instance object if commit=True. Otherwise, add
        a save_m2m() method to the form which can be called after the instance
        is saved manually at a later time. Return the model instance.
        """
        ...
    


class ModelForm(BaseModelForm, metaclass=ModelFormMetaclass):
    ...


def modelform_factory(model, form=..., fields=..., exclude=..., formfield_callback=..., widgets=..., localized_fields=..., labels=..., help_texts=..., error_messages=..., field_classes=...): # -> Any:
    """
    Return a ModelForm containing form fields for the given model. You can
    optionally pass a `form` argument to use as a starting point for
    constructing the ModelForm.

    ``fields`` is an optional list of field names. If provided, include only
    the named fields in the returned fields. If omitted or '__all__', use all
    fields.

    ``exclude`` is an optional list of field names. If provided, exclude the
    named fields from the returned fields, even if they are listed in the
    ``fields`` argument.

    ``widgets`` is a dictionary of model field names mapped to a widget.

    ``localized_fields`` is a list of names of fields which should be localized.

    ``formfield_callback`` is a callable that takes a model field and returns
    a form field.

    ``labels`` is a dictionary of model field names mapped to a label.

    ``help_texts`` is a dictionary of model field names mapped to a help text.

    ``error_messages`` is a dictionary of model field names mapped to a
    dictionary of error messages.

    ``field_classes`` is a dictionary of model field names mapped to a form
    field class.
    """
    ...

class BaseModelFormSet(BaseFormSet):
    """
    A ``FormSet`` for editing a queryset and/or adding new objects to it.
    """
    model = ...
    edit_only = ...
    unique_fields = ...
    def __init__(self, data=..., files=..., auto_id=..., prefix=..., queryset=..., *, initial=..., **kwargs) -> None:
        ...
    
    def initial_form_count(self): # -> int:
        """Return the number of forms that are required in this FormSet."""
        ...
    
    def get_queryset(self):
        ...
    
    def save_new(self, form, commit=...):
        """Save and return a new model instance for the given form."""
        ...
    
    def save_existing(self, form, instance, commit=...):
        """Save and return an existing model instance for the given form."""
        ...
    
    def delete_existing(self, obj, commit=...): # -> None:
        """Deletes an existing model instance."""
        ...
    
    def save(self, commit=...): # -> list[Unknown]:
        """
        Save model instances for every form, adding and changing instances
        as necessary, and return the list of instances.
        """
        ...
    
    def clean(self): # -> None:
        ...
    
    def validate_unique(self): # -> None:
        ...
    
    def get_unique_error_message(self, unique_check): # -> Any:
        ...
    
    def get_date_error_message(self, date_check): # -> Any:
        ...
    
    def get_form_error(self): # -> Any:
        ...
    
    def save_existing_objects(self, commit=...): # -> list[Unknown]:
        ...
    
    def save_new_objects(self, commit=...): # -> list[Unknown]:
        ...
    
    def add_fields(self, form, index): # -> None:
        """Add a hidden field for the object's primary key."""
        ...
    


def modelformset_factory(model, form=..., formfield_callback=..., formset=..., extra=..., can_delete=..., can_order=..., max_num=..., fields=..., exclude=..., widgets=..., validate_max=..., localized_fields=..., labels=..., help_texts=..., error_messages=..., min_num=..., validate_min=..., field_classes=..., absolute_max=..., can_delete_extra=..., renderer=..., edit_only=...): # -> Any:
    """Return a FormSet class for the given Django model class."""
    ...

class BaseInlineFormSet(BaseModelFormSet):
    """A formset for child objects related to a parent."""
    def __init__(self, data=..., files=..., instance=..., save_as_new=..., prefix=..., queryset=..., **kwargs) -> None:
        ...
    
    def initial_form_count(self): # -> int:
        ...
    
    @classmethod
    def get_default_prefix(cls):
        ...
    
    def save_new(self, form, commit=...):
        ...
    
    def add_fields(self, form, index): # -> None:
        ...
    
    def get_unique_error_message(self, unique_check): # -> Any:
        ...
    


def inlineformset_factory(parent_model, model, form=..., formset=..., fk_name=..., fields=..., exclude=..., extra=..., can_order=..., can_delete=..., max_num=..., formfield_callback=..., widgets=..., validate_max=..., localized_fields=..., labels=..., help_texts=..., error_messages=..., min_num=..., validate_min=..., field_classes=..., absolute_max=..., can_delete_extra=..., renderer=..., edit_only=...): # -> Any:
    """
    Return an ``InlineFormSet`` for the given kwargs.

    ``fk_name`` must be provided if ``model`` has more than one ``ForeignKey``
    to ``parent_model``.
    """
    ...

class InlineForeignKeyField(Field):
    """
    A basic integer field that deals with validating the given value to a
    given parent instance in an inline.
    """
    widget = HiddenInput
    default_error_messages = ...
    def __init__(self, parent_instance, *args, pk_field=..., to_field=..., **kwargs) -> None:
        ...
    
    def clean(self, value): # -> Unknown | None:
        ...
    
    def has_changed(self, initial, data): # -> Literal[False]:
        ...
    


class ModelChoiceIteratorValue:
    def __init__(self, value, instance) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    


class ModelChoiceIterator:
    def __init__(self, field) -> None:
        ...
    
    def __iter__(self): # -> Generator[tuple[Literal[''], Unknown] | tuple[ModelChoiceIteratorValue, Unknown], None, None]:
        ...
    
    def __len__(self):
        ...
    
    def __bool__(self): # -> Literal[True]:
        ...
    
    def choice(self, obj): # -> tuple[ModelChoiceIteratorValue, Unknown]:
        ...
    


class ModelChoiceField(ChoiceField):
    """A ChoiceField whose choices are a model QuerySet."""
    default_error_messages = ...
    iterator = ModelChoiceIterator
    def __init__(self, queryset, *, empty_label=..., required=..., widget=..., label=..., initial=..., help_text=..., to_field_name=..., limit_choices_to=..., blank=..., **kwargs) -> None:
        ...
    
    def get_limit_choices_to(self): # -> None:
        """
        Return ``limit_choices_to`` for this form field.

        If it is a callable, invoke it and return the result.
        """
        ...
    
    def __deepcopy__(self, memo): # -> Self@ModelChoiceField:
        ...
    
    queryset = ...
    def label_from_instance(self, obj): # -> str:
        """
        Convert objects into strings and generate the labels for the choices
        presented by this object. Subclasses can override this method to
        customize the display of the choices.
        """
        ...
    
    choices = ...
    def prepare_value(self, value):
        ...
    
    def to_python(self, value): # -> Any | None:
        ...
    
    def validate(self, value): # -> None:
        ...
    
    def has_changed(self, initial, data): # -> bool:
        ...
    


class ModelMultipleChoiceField(ModelChoiceField):
    """A MultipleChoiceField whose choices are a model QuerySet."""
    widget = SelectMultiple
    hidden_widget = MultipleHiddenInput
    default_error_messages = ...
    def __init__(self, queryset, **kwargs) -> None:
        ...
    
    def to_python(self, value): # -> list[Unknown] | list[Any | Unknown]:
        ...
    
    def clean(self, value): # -> Any:
        ...
    
    def prepare_value(self, value): # -> list[Unknown]:
        ...
    
    def has_changed(self, initial, data): # -> bool:
        ...
    


def modelform_defines_fields(form_class): # -> bool:
    ...

