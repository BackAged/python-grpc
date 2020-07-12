import grpc
from domain.product import Product
from pb import product_pb2, product_pb2_grpc
from service.product.port import AbstractProductService
import uuid

class ProductHandler(product_pb2_grpc.ProductServiceServicer):
    def __init__(self, product_service: AbstractProductService):
        self.product_service = product_service

    def ToProtoProduct(self, product):
        return product_pb2.Product(
            code=product.code,
            productName=product.productName,
            quantity=product.quantity,
            price=product.price,
            imageLink=product.imageLink,
            description=product.description
        )

    def Hello(self, request, context):
        return product_pb2.HelloRes(message='Hello!')

    def CreateProduct(self, request, context):
        print("got called for createProduct")
        product = Product(
            code=str(uuid.uuid4()),
            productName=request.productName,
            quantity=request.quantity,
            price=request.price,
            imageLink=request.imageLink,
            description=request.description
        )

        product = self.product_service.add(product=product)
        return self.ToProtoProduct(product)

    def GetProduct(self, request, context):
        product = self.product_service.get_by_code(request.code)
        if not product:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Product Not Found')
            return product_pb2.Product()

        return self.ToProtoProduct(product)

    def ListProducts(self, request, context):
        products = self.product_service.list()

        
        for product in products:
            yield self.ToProtoProduct(product)
