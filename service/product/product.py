from repository.port import AbstractProductRepository
from domain.product import Product
from service.product.port import AbstractProductService


class ProductService(AbstractProductService):
    def __init__(self, repo: AbstractProductRepository):
        self.repo = repo

    def get_by_code(self, code: str) -> Product:
       return self.repo.get(code)

    def add(self, product: Product) -> Product:
        return self.repo.put(product)

    def list(self, skip = None, limit = None) -> [Product]:
       return self.repo.list()