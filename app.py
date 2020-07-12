from concurrent import futures
import logging
import grpc

from pb import product_pb2_grpc

from delivery_grpc.product import ProductHandler
from repository.product import ProductRepo
from service.product.product import ProductService


def serve():
    product_repository = ProductRepo()
    product_service = ProductService(product_repository)
    product_grpc_handler = ProductHandler(product_service)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductServiceServicer_to_server(product_grpc_handler, server)
    server.add_insecure_port('[::]:3000')
    print("starting server on: ", 3000)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()