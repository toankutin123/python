# 🚀 Hướng Dẫn Nhanh Bắt Đầu

## Bước 1: Chạy Chương Trình

```bash
python personnel_system.py
```

## Bước 2: Tải Dữ Liệu Mẫu (Tùy Chọn)

Nếu muốn có dữ liệu mẫu để kiểm tra:

```bash
python load_sample_data.py
```

Sau đó chạy lại: `python personnel_system.py`

## Bước 3: Sử Dụng Menu

```
1. Thêm mới nhân sự
   → Nhập CCCD, Tên, Ngày sinh, Giới tính, Địa chỉ

2. Sửa thông tin nhân sự
   → Nhập CCCD của nhân sự cần sửa
   → Chọn trường cần sửa

3. Xóa nhân sự
   → Nhập CCCD
   → Xác nhận xóa

4. Xem danh sách nhân sự
   → Hiển thị tất cả nhân sự

5. Tìm kiếm nhân sự
   → Theo CCCD, Tên, hoặc Địa chỉ

6. Thoát
```

## 📝 Ví Dụ Sử Dụng

### Ví Dụ 1: Thêm Nhân Sự Mới

```
Nhập số CCCD: 001234567895
Nhập họ và tên: Lê Anh F
Nhập ngày sinh (DD/MM/YYYY): 12/07/1993
Giới tính: (1) Nam, (2) Nữ
Chọn (1/2): 1
Nhập địa chỉ thường trú: 999 Đường Hai Bà Trưng, Hà Nội

✅ Thêm nhân sự thành công!
```

### Ví Dụ 2: Tìm Kiếm Theo Tên

```
Menu: Chọn 5 (Tìm kiếm)
Chọn: 2 (Theo tên)
Nhập tên: Nguyễn

✅ Tìm thấy 3 kết quả:
STT | CCCD | Tên | Ngày sinh | Giới tính | Địa chỉ
1   | 001234567890 | Nguyễn Văn A | 15/06/1990 | Nam | ...
2   | 001234567891 | Nguyễn Thị B | 20/03/1992 | Nữ | ...
...
```

### Ví Dụ 3: Sửa Thông Tin

```
Nhập số CCCD: 001234567890
Thông tin hiện tại: CCCD: 001234567890 | Tên: Nguyễn Văn A | ...

Chọn trường:
1. Tên
2. Ngày sinh
3. Giới tính
4. Địa chỉ
5. Sửa tất cả

Chọn: 1
Nhập tên mới: Nguyễn Văn Anh

✅ Cập nhật thông tin thành công!
```

## ⚡ Các Phím Tắt

- **Enter**: Xác nhận, tiếp tục
- **Ctrl+C**: Dừng chương trình (an toàn)
- **y/n**: Xác nhận/Hủy

## ⚠️ Lưu Ý Quan Trọng

1. **CCCD phải duy nhất** - Không thể thêm 2 người cùng CCCD
2. **Ngày sinh** - Phải nhập đúng định dạng DD/MM/YYYY
3. **Dữ liệu tự động lưu** - Không cần lưu thủ công
4. **File dữ liệu** - Lưu trong file `personnel_data.json`

## 🔧 Xử Lý Sự Cố

### Lỗi: File personnel_data.json không tìm thấy
→ Chương trình sẽ tự động tạo file khi bạn thêm người đầu tiên

### Lỗi: Định dạng ngày không hợp lệ
→ Chắc chắn nhập đúng định dạng: DD/MM/YYYY (ví dụ: 15/06/1990)

### Lỗi: CCCD đã tồn tại
→ Nhập số CCCD khác

### Lỗi: Không tìm thấy nhân sự
→ Kiểm tra lại CCCD hoặc tên, cộng chính xác ký tự

## 💡 Mẹo Sử Dụng

1. **Tìm kiếm theo phần của tên** - Không cần nhập đầy đủ tên
   - Ví dụ: Nhập "Anh" để tìm cả "Lê Anh" và "Trần Thị Anh"

2. **Tìm kiếm theo địa chỉ** - Có thể nhập thành phố hoặc quận
   - Ví dụ: Nhập "Hà Nội" để tìm tất cả nhân sự ở Hà Nội

3. **Sao lưu dữ liệu** - Sao chép file `personnel_data.json` để backup

4. **Sửa nhiều trường** - Chọn "5. Sửa tất cả" để sửa cùng lúc

## 📧 Hỗ Trợ

Nếu gặp vấn đề, kiểm tra:
- ✓ Python 3.6+ đã cài đặt
- ✓ File `personnel_system.py` tồn tại
- ✓ Quyền ghi trong thư mục dự án
- ✓ Terminal không bị lỗi encoding
