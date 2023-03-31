"""
This type stub file was generated by pyright.
"""

from django.dispatch import receiver
from django.utils.autoreload import autoreload_started, file_changed

def get_template_directories(): # -> set[Unknown]:
    ...

def reset_loaders(): # -> None:
    ...

@receiver(autoreload_started, dispatch_uid="template_loaders_watch_changes")
def watch_for_template_changes(sender, **kwargs): # -> None:
    ...

@receiver(file_changed, dispatch_uid="template_loaders_file_changed")
def template_changed(sender, file_path, **kwargs): # -> Literal[True] | None:
    ...

