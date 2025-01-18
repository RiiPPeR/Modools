from typing import List, Optional
from datetime import datetime
from ..employees.employee import Employee

class Project:
    id: int
    name: str
    description: str 
    start_date: datetime
    end_date: Optional[datetime]
    status: str
    assigned_employees: List[Employee]
    budget: float
    
    def __init__(self, id: int = None, name: str = None, description: str = None, 
                 start_date: datetime = None, end_date: datetime = None, 
                 status: str = None, assigned_employees: List[Employee] = None,
                 budget: float = None):
        self.id = id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date 
        self.status = status
        self.assigned_employees = assigned_employees or []
        self.budget = budget