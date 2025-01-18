from typing import List, Optional
from datetime import datetime

from backend.model.employees.employee import Employee

class Maintenance:
    id: int
    device_name: str
    description: str
    maintenance_date: datetime
    next_maintenance: datetime
    status: str
    technician: str
    cost: float
    
    def __init__(self, id: int = None, device_name: str = None, description: str = None, maintenance_date: datetime = None, next_maintenance: datetime = None, status: str = None, technician: Employee = None, cost: float = None):
        self.id = id
        self.device_name = device_name
        self.description = description
        self.maintenance_date = maintenance_date 
        self.next_maintenance = next_maintenance
        self.status = status
        self.technician = Employee
        self.cost = cost