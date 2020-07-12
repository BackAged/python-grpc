class Product():
    def __init__(self, code, productName, quantity, price, imageLink, description):
        self.code = code
        self.productName = productName
        self.quantity = quantity
        self.price = price
        self.imageLink = imageLink
        self.description = description

    @classmethod
    def from_dict(cls, dict):
        room = Product(
            code = dict['code'],
            productName = dict['productName'],
            quantity = dict['quantity'],
            price = dict['price'],
            imageLink = dict['imageLink'],
            description = dict['description'],
        )

        return room

    def to_dict(self):
        return {
            'code': self.code,
            'productName': self.productName,
            'quantity': self.quantity,
            'price': self.price,
            'imageLink': self.imageLink,
            'description': self.description,
        }