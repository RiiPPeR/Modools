from typing import List, Optional
from datetime import datetime

class Customer:
    id: int
    name: str
    email: str
    phone: str
    created_at: datetime
    updated_at: datetime

    def __init__(self, id: int = None, name: str = None, email: str = None, phone: str = None, created_at: datetime = None, updated_at: datetime = None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.created_at = created_at
        self.updated_at = updated_at