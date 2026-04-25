"""
Hệ thống quản lý nhân sự
Personnel Management System
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class Person:
    """Class đại diện cho một nhân viên"""
    
    def __init__(self, cccd: str, name: str, dob: str, gender: str, address: str):
        """
        Khởi tạo thông tin nhân sự
        Args:
            cccd: Số chứng chỉ căn cước
            name: Họ và tên
            dob: Ngày sinh (DD/MM/YYYY)
            gender: Giới tính (Nam/Nữ)
            address: Địa chỉ thường trú
        """
        self.cccd = cccd
        self.name = name
        self.dob = dob
        self.gender = gender
        self.address = address
    
    def to_dict(self) -> Dict:
        """Chuyển đối tượng thành dictionary"""
        return {
            "cccd": self.cccd,
            "name": self.name,
            "dob": self.dob,
            "gender": self.gender,
            "address": self.address
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Person':
        """Tạo đối tượng từ dictionary"""
        return Person(
            data["cccd"],
            data["name"],
            data["dob"],
            data["gender"],
            data["address"]
        )
    
    def __str__(self) -> str:
        return f"CCCD: {self.cccd} | Tên: {self.name} | NSN: {self.dob} | GT: {self.gender} | Địa chỉ: {self.address}"
    
    def __repr__(self) -> str:
        return self.__str__()


class PersonnelDatabase:
    """Class quản lý cơ sở dữ liệu nhân sự"""
    
    def __init__(self, filename: str = "personnel_data.json"):
        """
        Khởi tạo cơ sở dữ liệu
        Args:
            filename: Tên file lưu dữ liệu
        """
        self.filename = filename
        self.personnel: List[Person] = []
        self.load_data()
    
    def load_data(self) -> None:
        """Tải dữ liệu từ file JSON"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.personnel = [Person.from_dict(p) for p in data]
        except Exception as e:
            print(f"Lỗi khi tải dữ liệu: {e}")
            self.personnel = []
    
    def save_data(self) -> None:
        """Lưu dữ liệu vào file JSON"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump([p.to_dict() for p in self.personnel], f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Lỗi khi lưu dữ liệu: {e}")
    
    def add_person(self, person: Person) -> bool:
        """
        Thêm nhân sự mới
        Args:
            person: Đối tượng Person cần thêm
        Returns:
            True nếu thêm thành công, False nếu CCCD đã tồn tại
        """
        # Kiểm tra CCCD có trùng không
        if self.find_by_cccd(person.cccd):
            return False
        
        self.personnel.append(person)
        self.save_data()
        return True
    
    def find_by_cccd(self, cccd: str) -> Optional[Person]:
        """Tìm nhân sự theo số CCCD"""
        for person in self.personnel:
            if person.cccd == cccd:
                return person
        return None
    
    def find_by_name(self, name: str) -> List[Person]:
        """Tìm nhân sự theo tên (tìm kiếm từng phần)"""
        return [p for p in self.personnel if name.lower() in p.name.lower()]
    
    def find_by_address(self, address: str) -> List[Person]:
        """Tìm nhân sự theo địa chỉ (tìm kiếm từng phần)"""
        return [p for p in self.personnel if address.lower() in p.address.lower()]
    
    def update_person(self, cccd: str, name: str = None, dob: str = None, 
                      gender: str = None, address: str = None) -> bool:
        """
        Cập nhật thông tin nhân sự
        Args:
            cccd: Số CCCD (không thể thay đổi)
            name: Họ và tên (nếu muốn sửa)
            dob: Ngày sinh (nếu muốn sửa)
            gender: Giới tính (nếu muốn sửa)
            address: Địa chỉ (nếu muốn sửa)
        Returns:
            True nếu cập nhật thành công, False nếu không tìm thấy
        """
        person = self.find_by_cccd(cccd)
        if not person:
            return False
        
        if name is not None:
            person.name = name
        if dob is not None:
            person.dob = dob
        if gender is not None:
            person.gender = gender
        if address is not None:
            person.address = address
        
        self.save_data()
        return True
    
    def delete_person(self, cccd: str) -> bool:
        """
        Xóa nhân sự
        Args:
            cccd: Số CCCD
        Returns:
            True nếu xóa thành công, False nếu không tìm thấy
        """
        person = self.find_by_cccd(cccd)
        if not person:
            return False
        
        self.personnel.remove(person)
        self.save_data()
        return True
    
    def get_all(self) -> List[Person]:
        """Lấy danh sách tất cả nhân sự"""
        return self.personnel
    
    def count(self) -> int:
        """Đếm tổng số nhân sự"""
        return len(self.personnel)


class PersonnelUI:
    """Class quản lý giao diện người dùng"""
    
    def __init__(self):
        """Khởi tạo giao diện"""
        self.db = PersonnelDatabase()
    
    @staticmethod
    def clear_screen() -> None:
        """Xóa màn hình"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_menu() -> None:
        """Hiển thị menu chính"""
        print("\n" + "="*70)
        print("        HỆ THỐNG QUẢN LÝ THÔNG TIN NHÂN SỰ")
        print("="*70)
        print("1. Thêm mới nhân sự")
        print("2. Sửa thông tin nhân sự")
        print("3. Xóa nhân sự")
        print("4. Xem danh sách nhân sự")
        print("5. Tìm kiếm nhân sự")
        print("6. Thoát chương trình")
        print("="*70)
    
    def add_person_prompt(self) -> None:
        """Nhập thông tin và thêm nhân sự mới"""
        print("\n--- THÊM NHÂN SỰ MỚI ---")
        try:
            cccd = input("Nhập số CCCD: ").strip()
            
            # Kiểm tra CCCD đã tồn tại
            if self.db.find_by_cccd(cccd):
                print("❌ CCCD này đã tồn tại trong hệ thống!")
                return
            
            name = input("Nhập họ và tên: ").strip()
            dob = input("Nhập ngày sinh (DD/MM/YYYY): ").strip()
            
            # Kiểm tra định dạng ngày sinh
            if not self.validate_date(dob):
                print("❌ Định dạng ngày sinh không hợp lệ!")
                return
            
            print("Giới tính: (1) Nam, (2) Nữ")
            gender_choice = input("Chọn (1/2): ").strip()
            gender = "Nam" if gender_choice == "1" else ("Nữ" if gender_choice == "2" else None)
            
            if gender is None:
                print("❌ Lựa chọn không hợp lệ!")
                return
            
            address = input("Nhập địa chỉ thường trú: ").strip()
            
            person = Person(cccd, name, dob, gender, address)
            
            if self.db.add_person(person):
                print("✅ Thêm nhân sự thành công!")
            else:
                print("❌ Không thể thêm nhân sự!")
        
        except Exception as e:
            print(f"❌ Lỗi: {e}")
    
    def edit_person_prompt(self) -> None:
        """Sửa thông tin nhân sự"""
        print("\n--- SỬA THÔNG TIN NHÂN SỰ ---")
        try:
            cccd = input("Nhập số CCCD của nhân sự cần sửa: ").strip()
            
            person = self.db.find_by_cccd(cccd)
            if not person:
                print("❌ Không tìm thấy nhân sự này!")
                return
            
            print(f"\nThông tin hiện tại: {person}")
            print("\nCác trường có thể sửa:")
            print("1. Tên")
            print("2. Ngày sinh")
            print("3. Giới tính")
            print("4. Địa chỉ")
            print("5. Sửa tất cả")
            
            choice = input("Chọn trường cần sửa (1-5): ").strip()
            
            updated = False
            
            if choice in ["1", "5"]:
                new_name = input(f"Nhập tên mới (hiện tại: {person.name}): ").strip()
                if new_name:
                    updated = self.db.update_person(cccd, name=new_name)
            
            if choice in ["2", "5"]:
                new_dob = input(f"Nhập ngày sinh mới (hiện tại: {person.dob}): ").strip()
                if new_dob and self.validate_date(new_dob):
                    updated = self.db.update_person(cccd, dob=new_dob)
                elif new_dob:
                    print("❌ Định dạng ngày sinh không hợp lệ!")
            
            if choice in ["3", "5"]:
                print("Giới tính: (1) Nam, (2) Nữ")
                gender_choice = input(f"Chọn giới tính (1/2, hiện tại: {person.gender}): ").strip()
                new_gender = "Nam" if gender_choice == "1" else ("Nữ" if gender_choice == "2" else None)
                if new_gender:
                    updated = self.db.update_person(cccd, gender=new_gender)
            
            if choice in ["4", "5"]:
                new_address = input(f"Nhập địa chỉ mới (hiện tại: {person.address}): ").strip()
                if new_address:
                    updated = self.db.update_person(cccd, address=new_address)
            
            if updated:
                print("✅ Cập nhật thông tin thành công!")
            elif choice not in ["1", "2", "3", "4", "5"]:
                print("❌ Lựa chọn không hợp lệ!")
        
        except Exception as e:
            print(f"❌ Lỗi: {e}")
    
    def delete_person_prompt(self) -> None:
        """Xóa nhân sự"""
        print("\n--- XÓA NHÂN SỰ ---")
        try:
            cccd = input("Nhập số CCCD của nhân sự cần xóa: ").strip()
            
            person = self.db.find_by_cccd(cccd)
            if not person:
                print("❌ Không tìm thấy nhân sự này!")
                return
            
            print(f"Nhân sự cần xóa: {person}")
            confirm = input("Bạn chắc chắn muốn xóa? (y/n): ").strip().lower()
            
            if confirm == 'y':
                if self.db.delete_person(cccd):
                    print("✅ Xóa nhân sự thành công!")
                else:
                    print("❌ Không thể xóa nhân sự!")
            else:
                print("Đã hủy thao tác xóa.")
        
        except Exception as e:
            print(f"❌ Lỗi: {e}")
    
    def view_all_prompt(self) -> None:
        """Xem danh sách tất cả nhân sự"""
        print("\n--- DANH SÁCH NHÂN SỰ ---")
        
        personnel = self.db.get_all()
        
        if not personnel:
            print("Hiện chưa có nhân sự nào trong hệ thống.")
            return
        
        print(f"Tổng số nhân sự: {len(personnel)}\n")
        print("-" * 120)
        print(f"{'STT':<5} {'CCCD':<15} {'Họ và tên':<25} {'Ngày sinh':<15} {'Giới tính':<10} {'Địa chỉ':<50}")
        print("-" * 120)
        
        for idx, person in enumerate(personnel, 1):
            print(f"{idx:<5} {person.cccd:<15} {person.name:<25} {person.dob:<15} {person.gender:<10} {person.address:<50}")
        
        print("-" * 120)
    
    def search_menu(self) -> None:
        """Menu tìm kiếm nhân sự"""
        print("\n--- TÌM KIẾM NHÂN SỰ ---")
        print("1. Tìm kiếm theo số CCCD")
        print("2. Tìm kiếm theo tên")
        print("3. Tìm kiếm theo địa chỉ")
        
        choice = input("Chọn (1-3): ").strip()
        
        if choice == "1":
            self.search_by_cccd()
        elif choice == "2":
            self.search_by_name()
        elif choice == "3":
            self.search_by_address()
        else:
            print("❌ Lựa chọn không hợp lệ!")
    
    def search_by_cccd(self) -> None:
        """Tìm kiếm theo CCCD"""
        cccd = input("Nhập số CCCD: ").strip()
        person = self.db.find_by_cccd(cccd)
        
        if person:
            print(f"\n✅ Kết quả tìm kiếm: {person}")
        else:
            print("❌ Không tìm thấy nhân sự này!")
    
    def search_by_name(self) -> None:
        """Tìm kiếm theo tên"""
        name = input("Nhập tên (hoặc một phần của tên): ").strip()
        results = self.db.find_by_name(name)
        
        if results:
            print(f"\n✅ Tìm thấy {len(results)} kết quả:")
            print("-" * 120)
            print(f"{'STT':<5} {'CCCD':<15} {'Họ và tên':<25} {'Ngày sinh':<15} {'Giới tính':<10} {'Địa chỉ':<50}")
            print("-" * 120)
            
            for idx, person in enumerate(results, 1):
                print(f"{idx:<5} {person.cccd:<15} {person.name:<25} {person.dob:<15} {person.gender:<10} {person.address:<50}")
            
            print("-" * 120)
        else:
            print("❌ Không tìm thấy nhân sự nào!")
    
    def search_by_address(self) -> None:
        """Tìm kiếm theo địa chỉ"""
        address = input("Nhập địa chỉ (hoặc một phần của địa chỉ): ").strip()
        results = self.db.find_by_address(address)
        
        if results:
            print(f"\n✅ Tìm thấy {len(results)} kết quả:")
            print("-" * 120)
            print(f"{'STT':<5} {'CCCD':<15} {'Họ và tên':<25} {'Ngày sinh':<15} {'Giới tính':<10} {'Địa chỉ':<50}")
            print("-" * 120)
            
            for idx, person in enumerate(results, 1):
                print(f"{idx:<5} {person.cccd:<15} {person.name:<25} {person.dob:<15} {person.gender:<10} {person.address:<50}")
            
            print("-" * 120)
        else:
            print("❌ Không tìm thấy nhân sự nào!")
    
    @staticmethod
    def validate_date(date_str: str) -> bool:
        """Kiểm tra định dạng ngày (DD/MM/YYYY)"""
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False
    
    def run(self) -> None:
        """Chạy chương trình chính"""
        while True:
            try:
                self.print_menu()
                choice = input("Nhập lựa chọn (1-6): ").strip()
                
                if choice == "1":
                    self.add_person_prompt()
                elif choice == "2":
                    self.edit_person_prompt()
                elif choice == "3":
                    self.delete_person_prompt()
                elif choice == "4":
                    self.view_all_prompt()
                elif choice == "5":
                    self.search_menu()
                elif choice == "6":
                    print("\n👋 Tạm biệt! Chương trình kết thúc.")
                    break
                else:
                    print("❌ Lựa chọn không hợp lệ! Vui lòng chọn từ 1-6.")
                
                input("\nNhấn Enter để tiếp tục...")
            
            except KeyboardInterrupt:
                print("\n\n👋 Chương trình bị dừng bởi người dùng.")
                break
            except Exception as e:
                print(f"❌ Lỗi: {e}")
                input("Nhấn Enter để tiếp tục...")


def main():
    """Hàm main"""
    ui = PersonnelUI()
    ui.run()


if __name__ == "__main__":
    main()
