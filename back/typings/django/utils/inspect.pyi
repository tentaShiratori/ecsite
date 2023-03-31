"""
This type stub file was generated by pyright.
"""

def get_func_args(func): # -> list[str]:
    ...

def get_func_full_args(func): # -> list[Unknown]:
    """
    Return a list of (argument name, default value) tuples. If the argument
    does not have a default value, omit it in the tuple. Arguments such as
    *args and **kwargs are also included.
    """
    ...

def func_accepts_kwargs(func): # -> bool:
    """Return True if function 'func' accepts keyword arguments **kwargs."""
    ...

def func_accepts_var_args(func): # -> bool:
    """
    Return True if function 'func' accepts positional arguments *args.
    """
    ...

def method_has_no_args(meth): # -> bool:
    """Return True if a method only accepts 'self'."""
    ...

def func_supports_parameter(func, name): # -> bool:
    ...

