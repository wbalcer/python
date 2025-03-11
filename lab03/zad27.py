class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def apply_discount(self, percent: float):
        if not (0 <= percent <= 100):
            raise ValueError("Discount percent must be between 0 and 100")
        self.price -= self.price * (percent / 100)

product = Product("a", 3000)
print(f"Cena przed: {product.price} zł")
product.apply_discount(10)
print(f"Cena po: {product.price} zł")