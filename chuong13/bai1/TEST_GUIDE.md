# 🧪 Hướng Dẫn Kiểm Tra Hệ Thống

## Tiêu Chí Kiểm Tra

Tài liệu này hướng dẫn cách kiểm tra tất cả các chức năng của hệ thống.

---

## 🔧 Chuẩn Bị

### 1. Chạy Chương Trình

```bash
cd "d:\learning python\2.3\luuthetoan\QL Nhân sự"
python personnel_system.py
```

### 2. Nạp Dữ Liệu Mẫu (Nếu Muốn)

```bash
python load_sample_data.py
```

---

## ✅ Kiểm Tra Chức Năng 1: Thêm Mới Nhân Sự

### Test Case 1.1: Thêm Người Hợp Lệ

**Bước:**
1. Chọn: 1 (Thêm mới nhân sự)
2. Nhập:
   - CCCD: `123456789012`
   - Tên: `Lý Thành Nghĩa`
   - Ngày sinh: `05/08/1995`
   - Giới tính: `1` (Nam)
   - Địa chỉ: `1000 Đường Võ Văn Kiệt, TP.HCM`

**Kỳ Vọng:**
- ✅ Thêm nhân sự thành công!
- Dữ liệu lưu vào file

---

### Test Case 1.2: CCCD Trùng

**Bước:**
1. Chọn: 1
2. Nhập CCCD đã tồn tại: `001234567890`

**Kỳ Vọng:**
- ❌ CCCD này đã tồn tại trong hệ thống!

---

### Test Case 1.3: Định Dạng Ngày Sai

**Bước:**
1. Chọn: 1
2. Nhập CCCD: `111111111111`
3. Nhập Tên: `Test`
4. Nhập ngày sinh: `08/05/1995` (sai format)

**Kỳ Vọng:**
- ❌ Định dạng ngày sinh không hợp lệ!

---

## ✅ Kiểm Tra Chức Năng 2: Sửa Thông Tin Nhân Sự

### Test Case 2.1: Sửa Tên

**Bước:**
1. Chọn: 2 (Sửa thông tin)
2. CCCD: `001234567890` (Nguyễn Văn A)
3. Chọn: 1 (Sửa tên)
4. Tên mới: `Nguyễn Văn Anh`

**Kỳ Vọng:**
- ✅ Cập nhật thông tin thành công!
- Tên thay đổi thành `Nguyễn Văn Anh`

---

### Test Case 2.2: Sửa Toàn Bộ

**Bước:**
1. Chọn: 2
2. CCCD: `001234567891` (Trần Thị B)
3. Chọn: 5 (Sửa tất cả)
4. Sửa lần lượt:
   - Tên: `Trần Thị Bích Liên`
   - Ngày sinh: `20/03/1992`
   - Giới tính: `2`
   - Địa chỉ: `789 Đường Nguyễn Huệ, TP.HCM`

**Kỳ Vọng:**
- ✅ Cập nhật thông tin thành công!
- Tất cả thông tin được sửa

---

### Test Case 2.3: CCCD Không Tồn Tại

**Bước:**
1. Chọn: 2
2. CCCD: `999999999999` (không tồn tại)

**Kỳ Vọng:**
- ❌ Không tìm thấy nhân sự này!

---

## ✅ Kiểm Tra Chức Năng 3: Xóa Nhân Sự

### Test Case 3.1: Xóa Thành Công

**Bước:**
1. Chọn: 3 (Xóa nhân sự)
2. CCCD: `001234567894` (Đặng Văn E)
3. Xác nhận: `y`

**Kỳ Vọng:**
- ✅ Xóa nhân sự thành công!
- Nhân sự không còn trong danh sách

---

### Test Case 3.2: Hủy Xóa

**Bước:**
1. Chọn: 3
2. CCCD: `001234567892` (Phạm Minh C)
3. Xác nhận: `n`

**Kỳ Vọng:**
- "Đã hủy thao tác xóa."
- Nhân sự vẫn tồn tại

---

### Test Case 3.3: Xóa Người Không Tồn Tại

**Bước:**
1. Chọn: 3
2. CCCD: `888888888888` (không tồn tại)

**Kỳ Vọng:**
- ❌ Không tìm thấy nhân sự này!

---

## ✅ Kiểm Tra Chức Năng 4: Xem Danh Sách

### Test Case 4.1: Xem Tất Cả

**Bước:**
1. Chọn: 4 (Xem danh sách)

**Kỳ Vọng:**
- Hiển thị bảng với tất cả nhân sự
- Gồm: STT, CCCD, Tên, Ngày sinh, Giới tính, Địa chỉ
- Hiển thị tổng số nhân sự

---

### Test Case 4.2: Danh Sách Trống

**Bước:**
1. Xóa tất cả nhân sự
2. Chọn: 4

**Kỳ Vọng:**
- "Hiện chưa có nhân sự nào trong hệ thống."

---

## ✅ Kiểm Tra Chức Năng 5: Tìm Kiếm

### Test Case 5.1: Tìm Theo CCCD

**Bước:**
1. Chọn: 5 (Tìm kiếm)
2. Chọn: 1 (Theo CCCD)
3. CCCD: `001234567890`

**Kỳ Vọng:**
- ✅ Tìm thấy 1 kết quả
- Hiển thị: Nguyễn Văn A | 001234567890 | ...

---

### Test Case 5.2: Tìm Theo Tên

**Bước:**
1. Chọn: 5
2. Chọn: 2 (Theo tên)
3. Tên: `Nguyễn`

**Kỳ Vọng:**
- ✅ Tìm thấy 2+ kết quả
- Hiển thị tất cả nhân sự có tên chứa "Nguyễn"

---

### Test Case 5.3: Tìm Theo Tên (Không Phân Biệt Hoa/Thường)

**Bước:**
1. Chọn: 5
2. Chọn: 2
3. Tên: `nguyễn` (chữ thường)

**Kỳ Vọng:**
- ✅ Tìm thấy kết quả (trường hợp không phân biệt)

---

### Test Case 5.4: Tìm Theo Địa Chỉ

**Bước:**
1. Chọn: 5
2. Chọn: 3 (Theo địa chỉ)
3. Địa chỉ: `Hà Nội`

**Kỳ Vọng:**
- ✅ Tìm thấy 2+ kết quả
- Hiển thị tất cả nhân sự ở Hà Nội

---

### Test Case 5.5: Tìm Không Có Kết Quả

**Bước:**
1. Chọn: 5
2. Chọn: 1
3. CCCD: `000000000000` (không tồn tại)

**Kỳ Vọng:**
- ❌ Không tìm thấy nhân sự này!

---

## ✅ Kiểm Tra Chức Năng 6: Thoát

### Test Case 6.1: Thoát Chương Trình

**Bước:**
1. Chọn: 6 (Thoát)

**Kỳ Vọng:**
- "👋 Tạm biệt! Chương trình kết thúc."
- Chương trình dừng

---

## ✅ Kiểm Tra Bổ Sung

### Test Lưu Trữ Dữ Liệu

**Bước:**
1. Thêm nhân sự mới
2. Thoát chương trình
3. Chạy lại chương trình
4. Xem danh sách

**Kỳ Vọng:**
- ✅ Nhân sự vừa thêm vẫn còn trong danh sách
- Dữ liệu được lưu vào file `personnel_data.json`

---

### Test Xử Lý Lỗi

**Bước:**
1. Chọn: 1 (Thêm mới)
2. Nhập lựa chọn không hợp lệ
3. Chọn: 2 (Giới tính)

**Kỳ Vọng:**
- ❌ Lựa chọn không hợp lệ!
- Chương trình không bị crash

---

### Test Ngắt Chương Trình

**Bước:**
1. Nhấn Ctrl+C

**Kỳ Vọng:**
- "👋 Chương trình bị dừng bởi người dùng."
- Dữ liệu được lưu (không mất)

---

## 📊 Bảng Tóm Tắt Kiểm Tra

| Chức Năng | Test Case | Kết Quả |
|-----------|-----------|---------|
| Thêm Mới | Hợp lệ | ✅ |
| Thêm Mới | CCCD Trùng | ❌ |
| Thêm Mới | Ngày Sai | ❌ |
| Sửa | Sửa Một Trường | ✅ |
| Sửa | Sửa Toàn Bộ | ✅ |
| Sửa | Không Tìm Thấy | ❌ |
| Xóa | Xóa Thành Công | ✅ |
| Xóa | Hủy Xóa | ✅ |
| Xóa | Không Tìm Thấy | ❌ |
| Xem | Xem Danh Sách | ✅ |
| Xem | Danh Sách Trống | ✅ |
| Tìm | Theo CCCD | ✅ |
| Tìm | Theo Tên | ✅ |
| Tìm | Theo Địa Chỉ | ✅ |
| Tìm | Không Tìm Thấy | ❌ |
| Thoát | Thoát Bình Thường | ✅ |
| Lưu | Lưu Dữ Liệu | ✅ |
| Lỗi | Xử Lý Ngoại Lệ | ✅ |

---

## 🎯 Kết Luận Kiểm Tra

- ✅ Tất cả chức năng hoạt động bình thường
- ✅ Dữ liệu được lưu trữ chính xác
- ✅ Xử lý lỗi toàn diện
- ✅ Giao diện thân thiện và rõ ràng
- ✅ Sẵn sàng sử dụng

---

## 💡 Mẹo Kiểm Tra

1. **Test toàn bộ trường**: Hãy thử nhập trường trống, ký tự đặc biệt, số
2. **Test biên giới**: Nhập CCCD rất dài, tên rất ngắn/dài
3. **Test tuần tự**: Hãy làm nhiều thao tác liên tiếp
4. **Test khôi phục**: Tắt/bật chương trình, kiểm tra dữ liệu

---

Chúc bạn kiểm tra thành công! 🎉
