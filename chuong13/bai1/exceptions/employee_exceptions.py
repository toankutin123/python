class EmployeeException(Exception):
    pass

class EmployeeNotFoundError(EmployeeException):
    def __init__(self, emp_id):
        super().__init__(f"Không tìm thấy ID: {emp_id}")

class InvalidSalaryError(EmployeeException):
    pass

class InvalidAgeError(EmployeeException):
    pass

class ProjectAllocationError(EmployeeException):
    pass

class DuplicateEmployeeError(EmployeeException):
    pass