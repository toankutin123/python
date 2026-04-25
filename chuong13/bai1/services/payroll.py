def total_salary(employees):
    return sum(e.calculate_salary() for e in employees)

def top3_salary(employees):
    return sorted(employees, key=lambda e: e.calculate_salary(), reverse=True)[:3]