 
from abc import ABCMeta, abstractmethod

from domain.product import Product

class AbstractProductService(metaclass=ABCMeta):
    @abstractmethod
    def get_by_code(self, code: str) -> Product:
       raise NotImplementedError()

    @abstractmethod
    def add(self, product: Product) -> Product:
        raise NotImplementedError()

    @abstractmethod
    def list(self, skip = None, limit = None) -> [Product]:
      raise NotImplementedError()
