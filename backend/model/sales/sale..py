from typing import List, Optional
from datetime import datetime
from ..inventory.product import Product
from ..crm import Customer

class Sale:
    id: int
    date: datetime
    customer: Customer
    products: List[Product]
    total_amount: float
    status: str
    payment_status: str

    def __init__(self, id: int = None, date: datetime = None, customer: Customer = None, products: List[Product] = None, total_amount: float = None, status: str = None, payment_status: str = None):
        self.id = id
        self.date = date
        self.customer = customer 
        self.products = products or []
        self.total_amount = total_amount
        self.status = status 
        self.payment_status = payment_status  