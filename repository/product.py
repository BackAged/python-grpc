from repository.errors import  DuplicateCodeError
from repository.port import AbstractProductRepository

class ProductRepo(AbstractProductRepository):
    """"
    very unefficient In Memory repository
    """

    def __init__(self, records = None):
        self._records = []
        if records:
            self._records.append(records)

    def get(self, code):
        filtered_products = list(filter(lambda product: product.code == code, self._records))
        if len(filtered_products) == 0:
            return None
        
        return filtered_products[0]

    def put(self, record):
        filtered_products = list(filter(lambda product: product.code == record.code, self._records))
        if len(filtered_products) != 0:
            raise DuplicateCodeError("Code already exists", None)
        
        self._records.append(record)
        return self._records[len(self._records) - 1]

    def list(self, skip = 0, limit = 10):
        return self._records[skip: skip+limit]