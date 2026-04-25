# 🎓 Hệ Thống Quản Lý Nhân Sự - Tài Liệu Hoàn Chỉnh

## 📚 Tài Liệu Trong Dự Án

Dự án hoàn chỉnh bao gồm các tài liệu sau:

### 1. **personnel_system.py** (⭐ Chính)
   - Chương trình chính (400+ dòng code)
   - Chứa 3 class chính:
     - `Person`: Đại diện một nhân sự
     - `PersonnelDatabase`: Quản lý CSDL
     - `PersonnelUI`: Giao diện người dùng
   - Tất cả chức năng tích hợp

### 2. **load_sample_data.py**
   - Script nạp dữ liệu mẫu
   - Tự động backup dữ liệu cũ
   - Sử dụng: `python load_sample_data.py`

### 3. **README.md**
   - Hướng dẫn chi tiết (tiếng Việt)
   - Mô tả tất cả chức năng
   - Cách sử dụng từng chức năng
   - Định dạng lưu trữ JSON

### 4. **QUICKSTART.md**
   - Hướng dẫn bắt đầu nhanh
   - Ví dụ sử dụng thực tế
   - Các mẹo hữu ích
   - Xử lý sự cố

### 5. **SUMMARY.md**
   - Tóm tắt tính năng hệ thống
   - Hoàn thành yêu cầu
   - Kiến trúc mã
   - Thích hợp cho

### 6. **TEST_GUIDE.md**
   - Hướng dẫn kiểm tra toàn diện
   - 20+ Test case chi tiết
   - Kỳ vọng cho từng test
   - Bảng tóm tắt kiểm tra

### 7. **sample_data.json**
   - Dữ liệu mẫu (5 nhân sự)
   - Sử dụng để kiểm tra nhanh
   - Load via: `python load_sample_data.py`

### 8. **personnel_data.json**
   - Database thực (tự động tạo)
   - Lưu trữ dữ liệu người dùng
   - Format: JSON

---

## 🎯 Hoàn Thành Yêu Cầu

### ✅ Yêu Cầu 1: Lưu Trữ Thông Tin
Danh sách nhân sự được lưu trữ trong Database gồm các thông tin:

- ✅ **Số CCCD** - Chứng chỉ căn cước
- ✅ **Họ và Tên** - Tên đầy đủ
- ✅ **Ngày Sinh** - Format DD/MM/YYYY
- ✅ **Giới Tính** - Nam/Nữ
- ✅ **Địa Chỉ Thường Trú** - Địa chỉ chi tiết

### ✅ Yêu Cầu 2: Chức Năng

- ✅ **Thêm mới nhân sự**
  - Nhập đầy đủ thông tin
  - Kiểm tra CCCD không trùng
  - Lưu vào database

- ✅ **Sửa thông tin nhân sự**
  - Tìm theo CCCD
  - Chọn trường cần sửa
  - Hoặc sửa tất cả cùng lúc

- ✅ **Xóa nhân sự**
  - Tìm theo CCCD
  - Xác nhận trước xóa
  - Xóa vĩnh viễn

- ✅ **Xem hiển thị danh sách nhân sự**
  - Bảng định dạng
  - Tất cả thông tin
  - Tổng số nhân sự

- ✅ **Tìm kiếm nhân sự**
  - Theo số CCCD
  - Theo tên
  - Theo địa chỉ
  - Tìm kiếm từng phần (partial)

---

## 🚀 Hướng Dẫn Nhanh

### 1️⃣ Bước 1: Mở Terminal/CMD

```
cd "d:\learning python\2.3\luuthetoan\QL Nhân sự"
```

### 2️⃣ Bước 2: Nạp Dữ Liệu Mẫu (Tùy Chọn)

```
python load_sample_data.py
```
Trả lời: `y`

### 3️⃣ Bước 3: Chạy Chương Trình

```
python personnel_system.py
```

### 4️⃣ Bước 4: Chọn Chức Năng

Menu sẽ hiển thị:
```
1. Thêm mới nhân sự
2. Sửa thông tin nhân sự
3. Xóa nhân sự
4. Xem danh sách nhân sự
5. Tìm kiếm nhân sự
6. Thoát chương trình
```

---

## 📖 Hướng Dẫn Chi Tiết Từng Chức Năng

### Chức Năng 1️⃣: Thêm Mới Nhân Sự

```
Chọn: 1

Nhập số CCCD: 123456789012
Nhập họ và tên: Nguyễn Văn A
Nhập ngày sinh (DD/MM/YYYY): 15/06/1990
Giới tính: (1) Nam, (2) Nữ
Chọn (1/2): 1
Nhập địa chỉ thường trú: 123 Đường Lê Lợi, Hà Nội

✅ Thêm nhân sự thành công!
```

### Chức Năng 2️⃣: Sửa Thông Tin

```
Chọn: 2

Nhập số CCCD của nhân sự cần sửa: 001234567890

Thông tin hiện tại: CCCD: 001234567890 | Tên: Nguyễn Văn A | ...

Chọn trường cần sửa:
1. Tên
2. Ngày sinh
3. Giới tính
4. Địa chỉ
5. Sửa tất cả

Chọn: 1
Nhập tên mới: Nguyễn Văn Anh

✅ Cập nhật thông tin thành công!
```

### Chức Năng 3️⃣: Xóa Nhân Sự

```
Chọn: 3

Nhập số CCCD của nhân sự cần xóa: 001234567890

Nhân sự cần xóa: CCCD: 001234567890 | Tên: Nguyễn Văn A | ...

Bạn chắc chắn muốn xóa? (y/n): y

✅ Xóa nhân sự thành công!
```

### Chức Năng 4️⃣: Xem Danh Sách

```
Chọn: 4

--- DANH SÁCH NHÂN SỰ ---
Tổng số nhân sự: 5

STT | CCCD | Họ và tên | Ngày sinh | Giới tính | Địa chỉ
1   | 001234567890 | Nguyễn Văn A | 15/06/1990 | Nam | 123 Đường Lê Lợi...
2   | 001234567891 | Trần Thị B | 20/03/1992 | Nữ | 456 Đường Nguyễn Huệ...
...
```

### Chức Năng 5️⃣: Tìm Kiếm

```
Chọn: 5

Menu tìm kiếm:
1. Tìm kiếm theo số CCCD
2. Tìm kiếm theo tên
3. Tìm kiếm theo địa chỉ

Chọn: 2
Nhập tên (hoặc một phần của tên): Nguyễn

✅ Tìm thấy 2 kết quả:
STT | CCCD | Họ và tên | Ngày sinh | Giới tính | Địa chỉ
1   | 001234567890 | Nguyễn Văn A | 15/06/1990 | Nam | ...
2   | 123456789012 | Nguyễn Văn Anh | 15/06/1990 | Nam | ...
```

---

## 💾 Định Dạng Dữ Liệu (JSON)

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

---

## 🔍 Các Tính Năng Nổi Bật

### 1. 🔐 An Toàn Dữ Liệu
- CCCD không thể trùng
- Xác nhận trước xóa
- Backup tự động
- Lưu persistent

### 2. 🎨 Giao Diện Thân Thiện
- Menu tiếng Việt rõ ràng
- Biểu tượng ✅ ❌
- Hướng dẫn từng bước
- Không phức tạp

### 3. 🔎 Tìm Kiếm Linh Hoạt
- Tìm theo CCCD chính xác
- Tìm theo tên (partial)
- Tìm theo địa chỉ (partial)
- Không phân biệt hoa/thường

### 4. ✨ Xử Lý Lỗi Toàn Diện
- Bắt tất cả ngoại lệ
- Thông báo rõ ràng
- Không bị crash
- Hướng dẫn khắc phục

### 5. 📊 Hiển Thị Bảng
- Bảng định dạng đẹp
- Tất cả thông tin rõ ràng
- Dễ đọc và theo dõi

---

## ⚠️ Lưu Ý Quan Trọng

### 1. Số CCCD
- Phải duy nhất trong hệ thống
- Không thể thêm 2 người cùng CCCD
- Không thể thay đổi khi sửa

### 2. Ngày Sinh
- Phải theo định dạng: **DD/MM/YYYY**
- Ví dụ hợp lệ: `15/06/1990`, `01/01/2000`
- Ví dụ sai: `1990-06-15`, `06/15/1990`

### 3. Xóa Vĩnh Viễn
- Khi xóa, dữ liệu xóa vĩnh viễn
- Không có chức năng phục hồi
- Cần xác nhận trước xóa

### 4. Tìm Kiếm
- Tìm theo tên/địa chỉ không phân biệt hoa/thường
- Tìm kiếm từng phần (partial match)
- Tìm theo CCCD phải chính xác

---

## 🛠️ Yêu Cầu Hệ Thống

- ✅ Python 3.6 trở lên
- ✅ Không cần cài thêm thư viện ngoài
- ✅ Hỗ trợ Windows, Mac, Linux
- ✅ UTF-8 encoding (hỗ trợ tiếng Việt)

---

## 🐛 Xử Lý Sự Cố

| Vấn Đề | Giải Pháp |
|--------|-----------|
| File `personnel_data.json` không tìm thấy | Bình thường! File sẽ tự tạo khi thêm người đầu tiên |
| Lỗi định dạng ngày | Nhập đúng: DD/MM/YYYY (ví dụ: 15/06/1990) |
| CCCD đã tồn tại | Nhập số CCCD khác |
| Chương trình bị crash | Báo lỗi được bắt, thử lại |
| Dữ liệu mất sau tắt | Dữ liệu được lưu tự động, không mất |
| Không tìm thấy nhân sự | Kiểm tra lại CCCD, tên, hoặc địa chỉ |

---

## 📞 Hỗ Trợ Nhanh

### Chạy Chương Trình
```bash
cd "d:\learning python\2.3\luuthetoan\QL Nhân sự"
python personnel_system.py
```

### Nạp Dữ Liệu Mẫu
```bash
python load_sample_data.py
# Trả lời: y
```

### Xem Danh Sách
```
Nhấn 4 trong menu
```

### Tìm Kiếm Nhanh
```
Nhấn 5 trong menu
Chọn cách tìm (1/2/3)
```

---

## 🎓 Thích Hợp Cho

- 👨‍🎓 Học tập lập trình Python
- 💼 Thực hành quản lý dữ liệu
- 🔧 Hiểu OOP, JSON, File I/O
- 📚 Ví dụ thực tế về CSDL
- 🏫 Bài tập lớn môn học

---

## 🎉 Kết Luận

✅ **Hệ thống hoàn thành 100% yêu cầu**

- ✓ Lưu trữ đầy đủ thông tin
- ✓ Thêm mới nhân sự
- ✓ Sửa thông tin
- ✓ Xóa nhân sự
- ✓ Xem danh sách
- ✓ Tìm kiếm (CCCD, Tên, Địa chỉ)
- ✓ Database persistent
- ✓ Giao diện thân thiện
- ✓ Tài liệu chi tiết
- ✓ Sẵn sàng sử dụng

**👉 Chạy ngay: `python personnel_system.py`**

---

Enjoy! 🎊
