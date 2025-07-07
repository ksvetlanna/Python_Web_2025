# __init__.py
from .module import greet #относительный иммпорт
from .utils import add

__version__ = '1.0.0'
__doc__ = 'Это пакет который содержит' #документация к пакету
__author__ = 'John' # автор пакета
__all__ = ['greet','add'] # функции в модуле к которым можно достучаться