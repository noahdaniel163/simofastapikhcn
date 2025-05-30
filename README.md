# SIMO FastAPI - Hệ thống gửi báo cáo khách hàng tổ chức qua API SBV

## 1. Giới thiệu
Ứng dụng này giúp gửi dữ liệu báo cáo các mã SIMO (001, 002, 003, 004) lên hệ thống SBV qua API. Hỗ trợ nhập liệu, kiểm thử, log kết quả/lỗi, chuyển đổi Excel-JSON, giao diện web thân thiện.

## 2. Yêu cầu hệ thống
- Python >= 3.8
- pip (Python package manager)
- SQL Server (nếu dùng truy vấn DB)
- Windows hoặc Linux đều chạy được

## 3. Cài đặt
1. Clone source code về máy:
   ```bash
   git clone <repo-url>
   cd simofastapikhcn
   ```
2. Cài đặt thư viện Python:
   ```bash
   pip install -r requirements.txt
   # Nếu chưa có requirements.txt:
   pip install fastapi uvicorn requests jinja2 pandas openpyxl pyodbc
   ```

## 4. Cấu hình hệ thống
### 4.1. Biến môi trường (khuyến nghị)
Tạo file `.env` (hoặc export/set biến môi trường):
```
SIMO_DB_SERVER=your_db_server
SIMO_DB_NAME=your_db_name
SIMO_DB_USER=your_db_user
SIMO_DB_PASSWORD=your_db_password
SIMO_USERNAME=your_sbv_user
SIMO_PASSWORD=your_sbv_pass
SIMO_CONSUMER_KEY=your_consumer_key
SIMO_CONSUMER_SECRET=your_consumer_secret
SIMO_TOKEN_URL=https://.../token
SIMO_ENTRYPOINT_URL_001=https://.../upload-bao-cao-danh-sach-tktt-khdn-api
# ... các biến khác tương tự ...
```
> **Không commit file .env, db_config.py, config.py chứa thông tin nhạy cảm lên git!**

### 4.2. File cấu hình nội bộ
- `db_config.py` và `config.py` sẽ tự động lấy giá trị từ biến môi trường.
- Không sửa trực tiếp thông tin thật trong source code.

## 5. Khởi động ứng dụng
- **Cách 1:**
  ```bash
  python launcher.py
  ```
- **Cách 2:**
  ```bash
  python main.py
  # hoặc
  uvicorn main:app --host 0.0.0.0 --port 8069 --reload
  ```
- Có thể đổi port bằng biến môi trường `SIMO_SERVER_PORT`.

## 6. Hướng dẫn sử dụng menu tính năng chương trình

- **Trang chủ:**
  - Chọn mã SIMO, nhập hoặc upload file JSON, gửi dữ liệu lên SBV.
- **Xử lý dữ liệu:**
  - Tìm kiếm, lọc, chọn dòng dữ liệu từ database.
  - Xuất JSON đúng chuẩn hoặc gửi trực tiếp lên SBV.
  - Hỗ trợ tìm kiếm realtime (AJAX) và server-side (SSR).
- **Chuyển Excel sang JSON:**
  - Chọn mã SIMO, upload file Excel mẫu, chuyển đổi sang JSON đúng schema.
  - Tải về file JSON kết quả.
- **Tải file Excel mẫu:**
  - Chọn mã SIMO, tải về file Excel mẫu đúng định dạng để nhập liệu.
- **Thống kê, biểu đồ:**
  - Xem thống kê tổng hợp, biểu đồ dữ liệu, thống kê tài khoản nghi ngờ gian lận.
- **Log dữ liệu:**
  - Xem lịch sử gửi nhận, phản hồi, lỗi của từng mã SIMO.
  - Lọc log theo mã SIMO.

## 7. Cấu trúc bảng dữ liệu (SQL Server)
Tạo bảng `tktt` với đầy đủ trường cho tất cả mã SIMO:
```sql
CREATE TABLE tktt (
    Cif NVARCHAR(50),
    SoID NVARCHAR(50),
    LoaiID INT,
    TenKhachHang NVARCHAR(255),
    NgaySinh NVARCHAR(20),
    GioiTinh INT,
    MaSoThue NVARCHAR(50),
    SoDienThoaiDangKyDichVu NVARCHAR(30),
    DiaChi NVARCHAR(255),
    DiaChiKiemSoatTruyCap NVARCHAR(50),
    MaSoNhanDangThietBiDiDong NVARCHAR(50),
    SoTaiKhoan NVARCHAR(50),
    LoaiTaiKhoan INT,
    TrangThaiHoatDongTaiKhoan INT,
    NgayMoTaiKhoan NVARCHAR(20),
    PhuongThucMoTaiKhoan INT,
    NgayXacThucTaiQuay NVARCHAR(20),
    GhiChu NVARCHAR(255),
    QuocTich NVARCHAR(50),
    NghiNgo INT,
    LyDoCapNhat NVARCHAR(255),
    UpdateDate DATETIME -- Ngày tháng ghi nhận dữ liệu thay đổi hoặc thêm mới
);
```
- Trường không dùng cho mã nào đó có thể để NULL.
- Tên trường, kiểu dữ liệu và thứ tự phải đồng nhất với file template Excel/JSON.

## 8. Mapping dữ liệu
- Khi import/export dữ liệu giữa Excel, JSON, Database phải dùng đúng tên và thứ tự trường như trên.
- Không thêm trường ngoài template JSON.
- Nếu cần trường nội bộ, đặt tên khác và không dùng khi gửi SBV.

## 9. Bảo mật
- Không commit file cấu hình thật lên git.
- Đổi toàn bộ mật khẩu, endpoint, khóa truy cập khi triển khai thực tế.
- Thư mục logs/ chỉ dùng kiểm thử, không public dữ liệu thật.

## 10. Troubleshooting
- Nếu lỗi kết nối DB: kiểm tra biến môi trường, file cấu hình, SQL Server.
- Nếu lỗi gửi SBV: kiểm tra endpoint, token, log trong logs/token.log.txt và logs/simo_00x.log.txt.
- Nếu lỗi import Excel: kiểm tra đúng file mẫu, đúng sheet, đúng tên trường.
- Nếu lỗi port: đổi biến môi trường `SIMO_SERVER_PORT`.

## 11. Tham khảo nhanh
- **Chạy server:** `python launcher.py` hoặc `python main.py`
- **Truy cập web:** http://localhost:8069/
- **Tải file mẫu:** Menu "Tải file Excel mẫu"
- **Chuyển Excel sang JSON:** Menu "Chuyển Excel sang JSON"
- **Xem log:** Menu "Log dữ liệu"

---
Mọi thắc mắc hoặc góp ý, vui lòng liên hệ đội phát triển hoặc admin hệ thống.