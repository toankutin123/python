from services.company import Company
from services.payroll import total_salary, top3_salary
from models.manager import Manager
from models.developer import Developer
from models.intern import Intern
from utils.validators import *
from exceptions.employee_exceptions import *
import os

company = Company()

# ===== UI =====
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("=" * 75)
    print("        HỆ THỐNG QUẢN LÝ NHÂN VIÊN CÔNG TY ABC")
    print("=" * 75)

    print("1. Thêm nhân viên mới")
    print("   a. Thêm Manager")
    print("   b. Thêm Developer")
    print("   c. Thêm Intern")

    print("\n2. Hiển thị danh sách nhân viên")
    print("   a. Tất cả nhân viên")
    print("   b. Theo loại")
    print("   c. Theo hiệu suất")

    print("\n3. Tìm kiếm nhân viên")
    print("   a. Theo ID")
    print("   b. Theo tên")
    print("   c. Theo ngôn ngữ (Developer)")

    print("\n4. Quản lý lương")
    print("   a. Lương từng nhân viên")
    print("   b. Tổng lương")
    print("   c. Top 3 lương cao")

    print("\n5. Quản lý dự án")
    print("   a. Thêm dự án")
    print("   b. Xóa dự án")
    print("   c. Hiển thị dự án")

    print("\n6. Đánh giá hiệu suất")
    print("   a. Cập nhật điểm")
    print("   b. Xuất sắc (>8)")
    print("   c. Cần cải thiện (<5)")

    print("\n7. Quản lý nhân sự")
    print("   a. Xóa nhân viên")
    print("   b. Tăng lương")
    print("   c. Thăng chức")

    print("\n8. Thống kê")
    print("   a. Số lượng theo loại")
    print("   b. Tổng lương")
    print("   c. Số dự án trung bình")

    print("\n9. Thoát")
    print("=" * 75)

# ===== INPUT =====
def input_employee():
    emp_id = input("ID: ")
    name = input("Tên: ")
    age = int(input("Tuổi: "))
    salary = float(input("Lương: "))

    validate_age(age)
    validate_salary(salary)

    return emp_id, name, age, salary

# ===== MAIN =====
while True:
    try:
        clear()
        menu()
        choice = input("Chọn (1-9): ")

        # ===== 1. THÊM =====
        if choice == "1":
            sub = input("Chọn (a/b/c): ")

            emp_id, name, age, salary = input_employee()

            if sub == "a":
                emp = Manager(emp_id, name, age, salary)

            elif sub == "b":
                lang = input("Ngôn ngữ: ")
                emp = Developer(emp_id, name, age, salary, lang)

            elif sub == "c":
                emp = Intern(emp_id, name, age, salary)

            else:
                raise ValueError("Sai lựa chọn")

            company.add_employee(emp)
            print("Thêm thành công")

        # ===== 2. HIỂN THỊ =====
        elif choice == "2":
            sub = input("Chọn (a/b/c): ")

            if sub == "a":
                company.list_employees()

            elif sub == "b":
                t = input("manager/developer/intern: ").lower()
                for e in company.filter_by_type(t):
                    print(e)

            elif sub == "c":
                for e in sorted(company.employees, key=lambda x: x.performance, reverse=True):
                    print(e.name, e.performance)

        # ===== 3. TÌM KIẾM =====
        elif choice == "3":
            sub = input("Chọn (a/b/c): ")

            if sub == "a":
                print(company.find_employee(input("ID: ")))

            elif sub == "b":
                for e in company.find_by_name(input("Tên: ")):
                    print(e)

            elif sub == "c":
                lang = input("Ngôn ngữ: ")
                for e in company.employees:
                    if isinstance(e, Developer) and e.language == lang:
                        print(e)

        # ===== 4. LƯƠNG =====
        elif choice == "4":
            sub = input("Chọn (a/b/c): ")

            if sub == "a":
                for e in company.employees:
                    print(e.name, e.calculate_salary())

            elif sub == "b":
                print("Tổng:", total_salary(company.employees))

            elif sub == "c":
                for e in top3_salary(company.employees):
                    print(e.name, e.calculate_salary())

        # ===== 5. PROJECT =====
        elif choice == "5":
            sub = input("Chọn (a/b/c): ")
            emp = company.find_employee(input("ID: "))

            if sub == "a":
                emp.add_project(input("Tên dự án: "))

            elif sub == "b":
                emp.remove_project(input("Tên dự án: "))

            elif sub == "c":
                print(emp.projects)

        # ===== 6. PERFORMANCE =====
        elif choice == "6":
            sub = input("Chọn (a/b/c): ")

            if sub == "a":
                emp = company.find_employee(input("ID: "))
                score = float(input("Điểm: "))
                if score < 0 or score > 10:
                    raise ValueError("0-10")
                emp.performance = score

            elif sub == "b":
                for e in company.employees:
                    if e.performance > 8:
                        print(e.name, e.performance)

            elif sub == "c":
                for e in company.employees:
                    if e.performance < 5:
                        print(e.name, e.performance)

        # ===== 7. NHÂN SỰ =====
        elif choice == "7":
            sub = input("Chọn (a/b/c): ")

            if sub == "a":
                company.delete_employee(input("ID: "))

            elif sub == "b":
                emp = company.find_employee(input("ID: "))
                emp.salary += float(input("Tăng: "))

            elif sub == "c":
                emp = company.find_employee(input("ID: "))
                emp.__class__ = Manager
                print("Đã thăng chức")

        # ===== 8. THỐNG KÊ =====
        elif choice == "8":
            sub = input("Chọn (a/b/c): ")

            if sub == "a":
                print("Manager:", len(company.filter_by_type("manager")))
                print("Developer:", len(company.filter_by_type("developer")))
                print("Intern:", len(company.filter_by_type("intern")))

            elif sub == "b":
                print("Tổng lương:", total_salary(company.employees))

            elif sub == "c":
                if company.employees:
                    avg = sum(len(e.projects) for e in company.employees) / len(company.employees)
                    print("TB dự án:", avg)

        elif choice == "9":
            break

        input("\nEnter để tiếp tục...")

    except Exception as e:
        print("Lỗi:", e)
        input("Enter để tiếp tục...")