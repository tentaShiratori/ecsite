"""
This type stub file was generated by pyright.
"""

from django.utils.functional import cached_property

class BaseEngine:
    def __init__(self, params) -> None:
        """
        Initialize the template engine.

        `params` is a dict of configuration settings.
        """
        ...
    
    @property
    def app_dirname(self):
        ...
    
    def from_string(self, template_code):
        """
        Create and return a template for the given source code.

        This method is optional.
        """
        ...
    
    def get_template(self, template_name):
        """
        Load and return a template for the given name.

        Raise TemplateDoesNotExist if no such template exists.
        """
        ...
    
    @cached_property
    def template_dirs(self): # -> tuple[Unknown, ...]:
        """
        Return a list of directories to search for templates.
        """
        ...
    
    def iter_template_filenames(self, template_name): # -> Generator[Unknown, None, None]:
        """
        Iterate over candidate files for template_name.

        Ignore files that don't lie inside configured template dirs to avoid
        directory traversal attacks.
        """
        ...
    


