# 📑 Chỉ Mục Hệ Thống Quản Lý Nhân Sự

## 🚀 Bắt Đầu (Chọn Một)

1. **👀 Tôi muốn xem nhanh** → [QUICKSTART.md](QUICKSTART.md)
2. **📖 Tôi muốn hiểu chi tiết** → [INSTRUCTIONS.md](INSTRUCTIONS.md)
3. **🎯 Tôi muốn toàn bộ thông tin** → [README.md](README.md)
4. **🧪 Tôi muốn kiểm tra hệ thống** → [TEST_GUIDE.md](TEST_GUIDE.md)

---

## 📂 Cấu Trúc Thư Mục

```
QL Nhân sự/
├── 📄 Tài Liệu Hướng Dẫn
│   ├── INDEX.md (File này)
│   ├── INSTRUCTIONS.md (Hướng dẫn hoàn chỉnh)
│   ├── QUICKSTART.md (Bắt đầu nhanh)
│   ├── README.md (Chi tiết đầy đủ)
│   ├── SUMMARY.md (Tóm tắt tính năng)
│   └── TEST_GUIDE.md (Hướng dẫn kiểm tra)
│
├── 🐍 Mã Python
│   ├── personnel_system.py (⭐ Chương trình chính)
│   └── load_sample_data.py (Nạp dữ liệu mẫu)
│
├── 📊 Dữ Liệu
│   ├── sample_data.json (Dữ liệu mẫu)
│   └── personnel_data.json (Database thực tế)
│
└── 📚 Thư Mục Khác
    ├── models/ (Cấu trúc cũ)
    ├── services/ (Cấu trúc cũ)
    ├── exceptions/ (Cấu trúc cũ)
    └── utils/ (Cấu trúc cũ)
```

---

## 🎯 Mục Đích Từng File

### 📖 Tài Liệu

| File | Mục Đích | Độ Dài | Khi Nào Đọc |
|------|----------|--------|------------|
| **INSTRUCTIONS.md** | Hướng dẫn hoàn chỉnh | Dài | Lần đầu chạy chương trình |
| **QUICKSTART.md** | Bắt đầu nhanh | Trung bình | Muốn chạy ngay lập tức |
| **README.md** | Chi tiết đầy đủ | Rất dài | Muốn biết chi tiết |
| **SUMMARY.md** | Tóm tắt tính năng | Trung bình | Xem tổng quát |
| **TEST_GUIDE.md** | Hướng dẫn kiểm tra | Dài | Muốn kiểm tra hết tính năng |
| **INDEX.md** | Chỉ mục (File này) | Ngắn | Định hướng nhanh |

### 🐍 Code

| File | Mục Đích | Dòng Code |
|------|----------|-----------|
| **personnel_system.py** | Chương trình chính | 400+ |
| **load_sample_data.py** | Nạp dữ liệu mẫu | 50+ |

### 📊 Dữ Liệu

| File | Mục Đích | Nội Dung |
|------|----------|---------|
| **sample_data.json** | Dữ liệu mẫu | 5 nhân sự |
| **personnel_data.json** | Database thực | Người dùng tạo |

---

## ⚡ Bắt Đầu Trong 3 Bước

### ✅ Bước 1: Mở Terminal

```
cd "d:\learning python\2.3\luuthetoan\QL Nhân sự"
```

### ✅ Bước 2: Nạp Dữ Liệu Mẫu (Tùy Chọn)

```
python load_sample_data.py
# Trả lời: y
```

### ✅ Bước 3: Chạy Chương Trình

```
python personnel_system.py
```

**Xong! 🎉**

---

## 🎮 Menu Chính (6 Lựa Chọn)

```
1. Thêm mới nhân sự
   → Nhập CCCD, Tên, Ngày sinh, Giới tính, Địa chỉ

2. Sửa thông tin nhân sự
   → Tìm theo CCCD → Chọn trường sửa

3. Xóa nhân sự
   → Tìm theo CCCD → Xác nhận xóa

4. Xem danh sách nhân sự
   → Hiển thị tất cả (bảng định dạng)

5. Tìm kiếm nhân sự
   → Theo CCCD, Tên, hoặc Địa chỉ

6. Thoát chương trình
   → Lưu dữ liệu và thoát
```

---

## ✅ Yêu Cầu Hoàn Thành

### Lưu Trữ Thông Tin
- ✓ Số CCCD
- ✓ Họ và tên
- ✓ Ngày sinh
- ✓ Giới tính
- ✓ Địa chỉ thường trú

### Chức Năng
- ✓ Thêm mới nhân sự
- ✓ Sửa thông tin nhân sự
- ✓ Xóa nhân sự
- ✓ Xem danh sách
- ✓ Tìm kiếm theo CCCD
- ✓ Tìm kiếm theo tên
- ✓ Tìm kiếm theo địa chỉ

---

## 📚 Học Tập

### Khái Niệm Python

- **OOP**: Class `Person`, `PersonnelDatabase`, `PersonnelUI`
- **JSON**: Lưu/tải dữ liệu từ file
- **File I/O**: Đọc/ghi file JSON
- **Exception Handling**: Xử lý lỗi
- **Data Structures**: List, Dictionary
- **String Methods**: Lower(), strip(), find()

### Cách Code

```python
# Class
class Person:
    def __init__(self, cccd, name, dob, gender, address):
        self.cccd = cccd
        self.name = name
        ...

# Lưu/Tải JSON
json.dump(data, f)
json.load(f)

# Exception
try:
    ...
except Exception as e:
    ...
```

---

## 🔧 Xử Lý Sự Cố

| Vấn Đề | Giải Pháp |
|--------|-----------|
| File không tìm thấy | File tự tạo lần đầu |
| Lỗi định dạng ngày | Dùng DD/MM/YYYY |
| CCCD trùng | Nhập khác |
| Chương trình bị lỗi | Nhấn Enter lại |
| Dữ liệu mất | Lưu tự động, không mất |

---

## 💡 Mẹo Sử Dụng

1. **Tìm kiếm từng phần**
   - Tên: Chỉ cần `Nguyễn` để tìm tất cả
   - Địa chỉ: Chỉ cần `Hà Nội` để tìm tất cả

2. **Sửa nhanh**
   - Chọn 5 (Sửa tất cả) để sửa cùng lúc

3. **Backup dữ liệu**
   - Sao chép `personnel_data.json` để backup

4. **Test nhanh**
   - Nạp dữ liệu mẫu: `python load_sample_data.py`

---

## 📞 Liên Hệ

### Chạy Chương Trình
```bash
python personnel_system.py
```

### Nạp Dữ Liệu Mẫu
```bash
python load_sample_data.py
```

### Xem Chi Tiết
- [INSTRUCTIONS.md](INSTRUCTIONS.md) - Hướng dẫn hoàn chỉnh
- [README.md](README.md) - Toàn bộ thông tin

---

## 🎓 Cho Giáo Viên

### Mục Đích Dạy Học

- ✓ Hiểu OOP (Class, Object)
- ✓ Làm việc với JSON
- ✓ File I/O trong Python
- ✓ Exception Handling
- ✓ Thiết kế giao diện
- ✓ Quản lý dữ liệu

### Độ Khó

- **Beginner**: Hiểu cấu trúc, chạy được
- **Intermediate**: Sửa/mở rộng chức năng
- **Advanced**: Thêm tính năng mới (DB, GUI)

### Mở Rộng Có Thể

1. Thêm GUI (tkinter, PyQt)
2. Thêm database (SQLite)
3. Thêm xác thực (login)
4. Thêm báo cáo (export PDF/Excel)
5. Thêm API (Flask, FastAPI)

---

## 🏆 Đã Hoàn Thành

- ✅ Tất cả yêu cầu
- ✅ Tài liệu chi tiết
- ✅ Dữ liệu mẫu
- ✅ Hướng dẫn kiểm tra
- ✅ Xử lý lỗi toàn diện
- ✅ Giao diện thân thiện
- ✅ Sẵn sàng sử dụng

---

## 🚀 Chạy Ngay

```bash
cd "d:\learning python\2.3\luuthetoan\QL Nhân sự"
python personnel_system.py
```

**Hãy bắt đầu! 🎊**

---

**Cập nhật**: Tháng 4 năm 2026
**Phiên bản**: 1.0
**Trạng thái**: Hoàn thành ✓
