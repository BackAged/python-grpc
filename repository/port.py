from abc import ABCMeta, abstractmethod

from domain.product import Product


class AbstractProductRepository(metaclass=ABCMeta):
    @abstractmethod
    def get(self, code: str) -> Product:
        raise NotImplementedError()

    @abstractmethod
    def put(self, record: Product) -> Product:
        raise NotImplementedError()

    @abstractmethod
    def list(self, skip: int, limit: int) -> [Product]:
        raise NotImplementedError()