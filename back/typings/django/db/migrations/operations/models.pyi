"""
This type stub file was generated by pyright.
"""

from django.db.migrations.operations.base import Operation
from django.utils.functional import cached_property

class ModelOperation(Operation):
    def __init__(self, name) -> None:
        ...
    
    @cached_property
    def name_lower(self):
        ...
    
    def references_model(self, name, app_label):
        ...
    
    def reduce(self, operation, app_label): # -> list[Unknown] | bool | list[Self@ModelOperation]:
        ...
    
    def can_reduce_through(self, operation, app_label): # -> bool:
        ...
    


class CreateModel(ModelOperation):
    """Create a model's table."""
    serialization_expand_args = ...
    def __init__(self, name, fields, options=..., bases=..., managers=...) -> None:
        ...
    
    def deconstruct(self): # -> tuple[str, list[Unknown], dict[str, Unknown]]:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def describe(self): # -> LiteralString:
        ...
    
    @property
    def migration_name_fragment(self): # -> cached_property:
        ...
    
    def references_model(self, name, app_label): # -> bool:
        ...
    
    def reduce(self, operation, app_label):
        ...
    


class DeleteModel(ModelOperation):
    """Drop a model's table."""
    def deconstruct(self): # -> tuple[str, list[Unknown], dict[str, Unknown]]:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def references_model(self, name, app_label): # -> Literal[True]:
        ...
    
    def describe(self): # -> LiteralString:
        ...
    
    @property
    def migration_name_fragment(self): # -> str:
        ...
    


class RenameModel(ModelOperation):
    """Rename a model."""
    def __init__(self, old_name, new_name) -> None:
        ...
    
    @cached_property
    def old_name_lower(self):
        ...
    
    @cached_property
    def new_name_lower(self):
        ...
    
    def deconstruct(self): # -> tuple[str, list[Unknown], dict[str, Unknown]]:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def references_model(self, name, app_label):
        ...
    
    def describe(self): # -> LiteralString:
        ...
    
    @property
    def migration_name_fragment(self): # -> str:
        ...
    
    def reduce(self, operation, app_label): # -> list[RenameModel] | list[Unknown | RenameModel] | bool | list[Self@Operation]:
        ...
    


class ModelOptionOperation(ModelOperation):
    def reduce(self, operation, app_label): # -> list[ModelOptionOperation | DeleteModel] | list[Unknown] | bool | list[Self@ModelOperation]:
        ...
    


class AlterModelTable(ModelOptionOperation):
    """Rename a model's table."""
    def __init__(self, name, table) -> None:
        ...
    
    def deconstruct(self): # -> tuple[str, list[Unknown], dict[str, Unknown]]:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def describe(self): # -> LiteralString:
        ...
    
    @property
    def migration_name_fragment(self): # -> str:
        ...
    


class AlterTogetherOptionOperation(ModelOptionOperation):
    option_name = ...
    def __init__(self, name, option_value) -> None:
        ...
    
    @cached_property
    def option_value(self): # -> Any:
        ...
    
    def deconstruct(self): # -> tuple[str, list[Unknown], dict[str | None, Unknown]]:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def references_field(self, model_name, name, app_label): # -> bool:
        ...
    
    def describe(self): # -> str:
        ...
    
    @property
    def migration_name_fragment(self): # -> str:
        ...
    
    def can_reduce_through(self, operation, app_label): # -> bool:
        ...
    


class AlterUniqueTogether(AlterTogetherOptionOperation):
    """
    Change the value of unique_together to the target one.
    Input value of unique_together must be a set of tuples.
    """
    option_name = ...
    def __init__(self, name, unique_together) -> None:
        ...
    


class AlterIndexTogether(AlterTogetherOptionOperation):
    """
    Change the value of index_together to the target one.
    Input value of index_together must be a set of tuples.
    """
    option_name = ...
    def __init__(self, name, index_together) -> None:
        ...
    


class AlterOrderWithRespectTo(ModelOptionOperation):
    """Represent a change with the order_with_respect_to option."""
    option_name = ...
    def __init__(self, name, order_with_respect_to) -> None:
        ...
    
    def deconstruct(self): # -> tuple[str, list[Unknown], dict[str, Unknown]]:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def references_field(self, model_name, name, app_label): # -> Literal[True]:
        ...
    
    def describe(self): # -> LiteralString:
        ...
    
    @property
    def migration_name_fragment(self): # -> str:
        ...
    


class AlterModelOptions(ModelOptionOperation):
    """
    Set new model options that don't directly affect the database schema
    (like verbose_name, permissions, ordering). Python code in migrations
    may still need them.
    """
    ALTER_OPTION_KEYS = ...
    def __init__(self, name, options) -> None:
        ...
    
    def deconstruct(self): # -> tuple[str, list[Unknown], dict[str, Unknown]]:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def describe(self): # -> LiteralString:
        ...
    
    @property
    def migration_name_fragment(self): # -> str:
        ...
    


class AlterModelManagers(ModelOptionOperation):
    """Alter the model's managers."""
    serialization_expand_args = ...
    def __init__(self, name, managers) -> None:
        ...
    
    def deconstruct(self): # -> tuple[str, list[Unknown], dict[Unknown, Unknown]]:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def describe(self): # -> LiteralString:
        ...
    
    @property
    def migration_name_fragment(self): # -> str:
        ...
    


class IndexOperation(Operation):
    option_name = ...
    @cached_property
    def model_name_lower(self):
        ...
    


class AddIndex(IndexOperation):
    """Add an index on a model."""
    def __init__(self, model_name, index) -> None:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def deconstruct(self): # -> tuple[str, list[Unknown], dict[str, Unknown]]:
        ...
    
    def describe(self): # -> str:
        ...
    
    @property
    def migration_name_fragment(self): # -> str:
        ...
    


class RemoveIndex(IndexOperation):
    """Remove an index from a model."""
    def __init__(self, model_name, name) -> None:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def deconstruct(self): # -> tuple[str, list[Unknown], dict[str, Unknown]]:
        ...
    
    def describe(self): # -> LiteralString:
        ...
    
    @property
    def migration_name_fragment(self): # -> str:
        ...
    


class RenameIndex(IndexOperation):
    """Rename an index."""
    def __init__(self, model_name, new_name, old_name=..., old_fields=...) -> None:
        ...
    
    @cached_property
    def old_name_lower(self):
        ...
    
    @cached_property
    def new_name_lower(self):
        ...
    
    def deconstruct(self): # -> tuple[str, list[Unknown], dict[str, Unknown]]:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def describe(self): # -> str:
        ...
    
    @property
    def migration_name_fragment(self): # -> str:
        ...
    
    def reduce(self, operation, app_label): # -> list[RenameIndex] | list[Unknown | RenameIndex] | list[Self@Operation] | Literal[False]:
        ...
    


class AddConstraint(IndexOperation):
    option_name = ...
    def __init__(self, model_name, constraint) -> None:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def deconstruct(self): # -> tuple[str, list[Unknown], dict[str, Unknown]]:
        ...
    
    def describe(self): # -> LiteralString:
        ...
    
    @property
    def migration_name_fragment(self): # -> str:
        ...
    


class RemoveConstraint(IndexOperation):
    option_name = ...
    def __init__(self, model_name, name) -> None:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def deconstruct(self): # -> tuple[str, list[Unknown], dict[str, Unknown]]:
        ...
    
    def describe(self): # -> LiteralString:
        ...
    
    @property
    def migration_name_fragment(self): # -> str:
        ...
    


