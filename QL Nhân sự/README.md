# Hệ Thống Quản Lý Thông Tin Nhân Sự

## 📋 Mô Tả

Chương trình quản lý thông tin nhân sự với các chức năng cơ bản:
- Thêm mới nhân sự
- Sửa thông tin nhân sự
- Xóa nhân sự
- Xem danh sách nhân sự
- Tìm kiếm nhân sự

## 📦 Cấu Trúc Dự Án

```
QL Nhân sự/
├── personnel_system.py      # Chương trình chính
├── personnel_data.json      # File lưu dữ liệu (tự động tạo)
├── README.md               # Hướng dẫn sử dụng
└── sample_data.json        # Dữ liệu mẫu
```

## 🚀 Hướng Dẫn Sử Dụng

### 1. Chạy Chương Trình

```bash
python personnel_system.py
```

### 2. Các Chức Năng

#### 2.1 Thêm Mới Nhân Sự
- Nhập số CCCD (chứng chỉ căn cước)
- Nhập họ và tên
- Nhập ngày sinh (định dạng DD/MM/YYYY)
- Chọn giới tính (Nam/Nữ)
- Nhập địa chỉ thường trú

**Lưu ý:** 
- Số CCCD phải là duy nhất
- Ngày sinh phải theo định dạng DD/MM/YYYY
- Tất cả thông tin bắt buộc phải nhập

#### 2.2 Sửa Thông Tin Nhân Sự
- Nhập số CCCD của nhân sự cần sửa
- Chọn trường cần sửa:
  1. Tên
  2. Ngày sinh
  3. Giới tính
  4. Địa chỉ
  5. Sửa tất cả
- Nhập thông tin mới

**Lưu ý:** Số CCCD không thể thay đổi

#### 2.3 Xóa Nhân Sự
- Nhập số CCCD của nhân sự cần xóa
- Xác nhận lệnh xóa (y/n)

#### 2.4 Xem Danh Sách Nhân Sự
- Hiển thị tất cả nhân sự trong hệ thống
- Bao gồm: STT, CCCD, Tên, Ngày sinh, Giới tính, Địa chỉ

#### 2.5 Tìm Kiếm Nhân Sự
Có 3 cách tìm kiếm:

##### a) Tìm Kiếm Theo CCCD
- Nhập đúng số CCCD
- Hiển thị 1 kết quả nếu tìm thấy

##### b) Tìm Kiếm Theo Tên
- Nhập tên hoặc một phần của tên
- Hiển thị tất cả kết quả khớp

##### c) Tìm Kiếm Theo Địa Chỉ
- Nhập địa chỉ hoặc một phần của địa chỉ
- Hiển thị tất cả kết quả khớp

## 💾 Lưu Trữ Dữ Liệu

### Định Dạng JSON

Dữ liệu được lưu trong file `personnel_data.json` với định dạng:

```json
[
  {
    "cccd": "001234567890",
    "name": "Nguyễn Văn A",
    "dob": "15/06/1990",
    "gender": "Nam",
    "address": "123 Đường Lê Lợi, Hà Nội"
  },
  {
    "cccd": "001234567891",
    "name": "Trần Thị B",
    "dob": "20/03/1992",
    "gender": "Nữ",
    "address": "456 Đường Nguyễn Huệ, TP.HCM"
  }
]
```

### Tính Năng Lưu Trữ
- Dữ liệu tự động lưu sau mỗi thao tác (thêm, sửa, xóa)
- File JSON được tạo tự động nếu chưa tồn tại
- Dữ liệu được bảo toàn giữa các phiên chạy chương trình

## 🔍 Các Ví Dụ

### Thêm Nhân Sự Mới
```
CCCD: 001234567890
Tên: Nguyễn Văn A
Ngày sinh: 15/06/1990
Giới tính: 1 (Nam)
Địa chỉ: 123 Đường Lê Lợi, Quận Hoàn Kiếm, Hà Nội
```

### Tìm Kiếm Theo Tên
```
Nhập tên: Nguyễn
→ Tìm thấy tất cả nhân sự có tên chứa "Nguyễn"
```

### Tìm Kiếm Theo Địa Chỉ
```
Nhập địa chỉ: Hà Nội
→ Tìm thấy tất cả nhân sự ở Hà Nội
```

## ⚠️ Lưu Ý Quan Trọng

1. **CCCD Duy Nhất:** Không thể thêm 2 nhân sự có cùng số CCCD
2. **Định Dạng Ngày:** Phải nhập đúng định dạng DD/MM/YYYY
3. **Xóa Vĩnh Viễn:** Khi xóa nhân sự, dữ liệu sẽ bị xóa vĩnh viễn (không khôi phục được)
4. **Tìm Kiếm Không Phân Biệt Hoa/Thường:** Các tìm kiếm theo tên/địa chỉ không phân biệt hoa/thường

## 🛠️ Yêu Cầu Hệ Thống

- Python 3.6 trở lên
- Không cần cài đặt thư viện bên ngoài (chỉ dùng thư viện chuẩn)

## 📝 Thông Tin Thêm

- **Ngôn ngữ:** Tiếng Việt
- **Độ khó:** Cơ bản
- **Thích hợp cho:** Học tập, bài tập thực hành

## 📞 Hỗ Trợ

Nếu gặp lỗi hoặc có câu hỏi, vui lòng kiểm tra:
1. Python đã được cài đặt đúng
2. File `personnel_system.py` nằm trong cùng thư mục
3. Quyền ghi file trong thư mục dự án
