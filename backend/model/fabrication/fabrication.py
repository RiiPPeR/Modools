from typing import List, Optional
from datetime import datetime
from backend.model.inventory.product import Product

class Fabrication:
    id: int
    product: Product
    start_date: datetime
    end_date: Optional[datetime]
    status: str
    quantity: int
    cost_per_unit: float
    
    def __init__(self, id: int = None, product: Product = None, start_date: datetime = None, end_date: datetime = None, status: str = None, quantity: int = None, cost_per_unit: float = None):
        self.id = id
        self.product = product
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit