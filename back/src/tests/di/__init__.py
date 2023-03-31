from injector import Injector
from src.di import modules
from .driver_module import MockDriverModule

test_modules = modules + [MockDriverModule()]
