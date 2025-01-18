from typing import List

class Product:
    id: int
    name: str
    description: str
    unit_cost: float
    price: float
    stock: int
    
    def __init__(self, id: int = None, name: str = None, description: str = None, unit_cost: float = None, price: float = None, stock: int = None):
        self.id = id
        self.name = name
        self.description = description
        self.unit_cost = unit_cost
        self.price = price
        self.stock = stock