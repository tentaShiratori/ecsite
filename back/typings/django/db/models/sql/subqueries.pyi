"""
This type stub file was generated by pyright.
"""

from django.db.models.sql.query import Query

"""
Query subclasses which provide extra functionality beyond simple data retrieval.
"""
__all__ = ["DeleteQuery", "UpdateQuery", "InsertQuery", "AggregateQuery"]
class DeleteQuery(Query):
    """A DELETE SQL query."""
    compiler = ...
    def do_query(self, table, where, using): # -> Any | Literal[0]:
        ...
    
    def delete_batch(self, pk_list, using): # -> Any | int:
        """
        Set up and execute delete queries for all the objects in pk_list.

        More than one physical query may be executed if there are a
        lot of values in pk_list.
        """
        ...
    


class UpdateQuery(Query):
    """An UPDATE SQL query."""
    compiler = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def clone(self): # -> Empty:
        ...
    
    def update_batch(self, pk_list, values, using): # -> None:
        ...
    
    def add_update_values(self, values): # -> None:
        """
        Convert a dictionary of field name to value mappings into an update
        query. This is the entry point for the public update() method on
        querysets.
        """
        ...
    
    def add_update_fields(self, values_seq): # -> None:
        """
        Append a sequence of (field, model, value) triples to the internal list
        that will be used to generate the UPDATE query. Might be more usefully
        called add_update_targets() to hint at the extra information here.
        """
        ...
    
    def add_related_update(self, model, field, value): # -> None:
        """
        Add (name, value) to an update query for an ancestor model.

        Update are coalesced so that only one update query per ancestor is run.
        """
        ...
    
    def get_related_updates(self): # -> list[Unknown]:
        """
        Return a list of query objects: one for each update required to an
        ancestor model. Each query will have the same filtering conditions as
        the current query but will only update a single table.
        """
        ...
    


class InsertQuery(Query):
    compiler = ...
    def __init__(self, *args, on_conflict=..., update_fields=..., unique_fields=..., **kwargs) -> None:
        ...
    
    def insert_values(self, fields, objs, raw=...): # -> None:
        ...
    


class AggregateQuery(Query):
    """
    Take another query as a parameter to the FROM clause and only select the
    elements in the provided list.
    """
    compiler = ...
    def __init__(self, model, inner_query) -> None:
        ...
    


