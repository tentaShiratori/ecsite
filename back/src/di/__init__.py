from injector import Injector
from .aws import AWSModule

modules = [AWSModule()]
injector = Injector(modules)
