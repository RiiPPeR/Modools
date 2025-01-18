from typing import List, Optional

class Employee:
    id: int
    name: str
    email: str
    position: str
    salary: float
    
    def __init__(self, id: int = None, name: str = None, email: str = None, position: str = None, salary: float = None):
        self.id = id
        self.name = name
        self.email = email
        self.position = position
        self.salary = salary

