from exceptions.employee_exceptions import *

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        for e in self.employees:
            if e.emp_id == emp.emp_id:
                raise DuplicateEmployeeError("Trùng ID")
        self.employees.append(emp)

    def find_employee(self, emp_id):
        for e in self.employees:
            if e.emp_id == emp_id:
                return e
        raise EmployeeNotFoundError(emp_id)

    def delete_employee(self, emp_id):
        emp = self.find_employee(emp_id)
        self.employees.remove(emp)

    def list_employees(self):
        if not self.employees:
            print("Chưa có dữ liệu")
        for e in self.employees:
            print(e)

    # ===== mở rộng =====
    def find_by_name(self, name):
        return [e for e in self.employees if name.lower() in e.name.lower()]

    def filter_by_type(self, t):
        return [e for e in self.employees if t in type(e).__name__.lower()]