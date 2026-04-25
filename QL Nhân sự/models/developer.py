from .employee import Employee

class Developer(Employee):
    def __init__(self, emp_id, name, age, salary, language=""):
        super().__init__(emp_id, name, age, salary)
        self.language = language

    def calculate_salary(self):
        return self.salary * 1.5