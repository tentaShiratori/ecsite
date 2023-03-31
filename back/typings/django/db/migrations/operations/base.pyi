"""
This type stub file was generated by pyright.
"""

class Operation:
    """
    Base class for migration operations.

    It's responsible for both mutating the in-memory model state
    (see db/migrations/state.py) to represent what it performs, as well
    as actually performing it against a live database.

    Note that some operations won't modify memory state at all (e.g. data
    copying operations), and some will need their modifications to be
    optionally specified by the user (e.g. custom Python code snippets)

    Due to the way this class deals with deconstruction, it should be
    considered immutable.
    """
    reversible = ...
    reduces_to_sql = ...
    atomic = ...
    elidable = ...
    serialization_expand_args = ...
    def __new__(cls, *args, **kwargs): # -> Self@Operation:
        ...
    
    def deconstruct(self): # -> tuple[str, Unknown, Unknown]:
        """
        Return a 3-tuple of class import path (or just name if it lives
        under django.db.migrations), positional arguments, and keyword
        arguments.
        """
        ...
    
    def state_forwards(self, app_label, state):
        """
        Take the state from the previous migration, and mutate it
        so that it matches what this migration would perform.
        """
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        """
        Perform the mutation on the database schema in the normal
        (forwards) direction.
        """
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        """
        Perform the mutation on the database schema in the reverse
        direction - e.g. if this were CreateModel, it would in fact
        drop the model's table.
        """
        ...
    
    def describe(self): # -> str:
        """
        Output a brief summary of what the action does.
        """
        ...
    
    @property
    def migration_name_fragment(self): # -> None:
        """
        A filename part suitable for automatically naming a migration
        containing this operation, or None if not applicable.
        """
        ...
    
    def references_model(self, name, app_label): # -> Literal[True]:
        """
        Return True if there is a chance this operation references the given
        model name (as a string), with an app label for accuracy.

        Used for optimization. If in doubt, return True;
        returning a false positive will merely make the optimizer a little
        less efficient, while returning a false negative may result in an
        unusable optimized migration.
        """
        ...
    
    def references_field(self, model_name, name, app_label): # -> Literal[True]:
        """
        Return True if there is a chance this operation references the given
        field name, with an app label for accuracy.

        Used for optimization. If in doubt, return True.
        """
        ...
    
    def allow_migrate_model(self, connection_alias, model): # -> bool:
        """
        Return whether or not a model may be migrated.

        This is a thin wrapper around router.allow_migrate_model() that
        preemptively rejects any proxy, swapped out, or unmanaged model.
        """
        ...
    
    def reduce(self, operation, app_label): # -> list[Unknown] | list[Self@Operation] | Literal[False]:
        """
        Return either a list of operations the actual operation should be
        replaced with or a boolean that indicates whether or not the specified
        operation can be optimized across.
        """
        ...
    
    def __repr__(self): # -> str:
        ...
    


