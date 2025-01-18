from typing import List, Optional
from datetime import datetime
from ..inventory.product import Product

class Purchase:
    id: int
    date: datetime
    supplier: str
    products: List[Product]
    total_amount: float
    status: str
    payment_status: str
    
    def __init__(self, id: int = None, date: datetime = None, supplier: str = None, products: List[Product] = None, total_amount: float = None, status: str = None, payment_status: str = None):
        self.id = id
        self.date = date
        self.supplier = supplier
        self.products = products or []
        self.total_amount = total_amount
        self.status = status  # e.g. 'pending', 'received', 'cancelled'
        self.payment_status = payment_status  # e.g. 'pending', 'paid', 'partial'