"""
Script để nạp dữ liệu mẫu vào cơ sở dữ liệu
Load sample data into the database
"""

import json
import shutil
import os

def load_sample_data():
    """Nạp dữ liệu mẫu từ sample_data.json sang personnel_data.json"""
    
    source_file = "sample_data.json"
    dest_file = "personnel_data.json"
    
    # Kiểm tra file mẫu có tồn tại không
    if not os.path.exists(source_file):
        print(f"❌ Lỗi: File {source_file} không tồn tại!")
        return
    
    # Backup file cũ nếu tồn tại
    if os.path.exists(dest_file):
        backup_file = f"personnel_data_backup_{len(os.listdir('.')) % 1000}.json"
        shutil.copy(dest_file, backup_file)
        print(f"✅ Đã sao lưu file cũ thành: {backup_file}")
    
    # Sao chép dữ liệu mẫu
    try:
        shutil.copy(source_file, dest_file)
        print(f"✅ Nạp dữ liệu mẫu thành công!")
        print(f"✅ Dữ liệu được lưu vào: {dest_file}")
        
        # Hiển thị số lượng dữ liệu đã nạp
        with open(dest_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"✅ Tổng số nhân sự: {len(data)}")
            print("\nDanh sách nhân sự mẫu:")
            for idx, person in enumerate(data, 1):
                print(f"  {idx}. {person['name']} - CCCD: {person['cccd']}")
    
    except Exception as e:
        print(f"❌ Lỗi khi nạp dữ liệu: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("Nạp Dữ Liệu Mẫu Vào Cơ Sở Dữ Liệu")
    print("=" * 60)
    
    confirm = input("Bạn có chắc chắn muốn nạp dữ liệu mẫu? (y/n): ").strip().lower()
    
    if confirm == 'y':
        load_sample_data()
    else:
        print("Đã hủy thao tác.")
