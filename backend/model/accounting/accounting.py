from typing import List, Optional
from datetime import datetime
from ..inventory.product import Product
from ..crm import Customer

class Transaction:
    id: int
    date: datetime
    description: str
    amount: float
    type: str 
    reference: str
    
    def __init__(self, id: int = None, date: datetime = None, description: str = None, amount: float = None, type: str = None, reference: str = None):
        self.id = id
        self.date = date
        self.description = description
        self.amount = amount
        self.type = type
        self.reference = reference

class Accounting:
    id: int
    transactions: List[Transaction]
    balance: float
    last_updated: datetime
    
    def __init__(self, id: int = None):
        self.id = id
        self.transactions = []
        self.balance = 0.0
        self.last_updated = datetime.now()
    
    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)
        if transaction.type == 'income':
            self.balance += transaction.amount
        else:
            self.balance -= transaction.amount
        self.last_updated = datetime.now()
    
    def get_balance(self) -> float:
        return self.balance
    
    def get_transactions(self, start_date: datetime = None, 
                        end_date: datetime = None) -> List[Transaction]:
        if not start_date and not end_date:
            return self.transactions
        
        filtered_transactions = []
        for transaction in self.transactions:
            if (not start_date or transaction.date >= start_date) and (not end_date or transaction.date <= end_date):
                filtered_transactions.append(transaction)
        return filtered_transactions