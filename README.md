# SIMO KHDN FastAPI - Hệ thống gửi báo cáo khách hàng tổ chức qua API SBV

## Mục đích
Ứng dụng này giúp gửi dữ liệu báo cáo các mã SIMO (001, 002, 003, 004) lên hệ thống SBV qua API, hỗ trợ nhập liệu, kiểm thử, log kết quả và lỗi, giao diện web thân thiện.

## Tính năng chính
- Giao diện web UI hiện đại, trực quan, hỗ trợ cả tìm kiếm realtime (AJAX) và tìm kiếm server-side render (SSR).
- Tìm kiếm, lọc, chọn nhiều dòng dữ liệu từ database (SQL Server) với bảng TKTT_TOCHUC.
- Chọn mã nghiệp vụ SIMO (001/002/003/004), xuất JSON đúng schema hoặc gửi trực tiếp lên endpoint SBV.
- Hỗ trợ nhập liệu, kiểm thử, log kết quả/lỗi, thao tác qua giao diện web.
- Tạo nhanh dữ liệu mẫu cho từng mã SIMO.
- Gửi dữ liệu lên endpoint SBV qua FastAPI backend.
- Log chi tiết từng lần gửi (payload, response, header, lỗi) vào file riêng cho từng mã.
- Cấu hình endpoint, tài khoản qua biến môi trường.
- Hỗ trợ chuyển đổi Excel sang JSON và tải file mẫu.
- Giao diện đẹp, responsive, có hiệu ứng loading, highlight từ khóa, phân trang.

## Cấu trúc thư mục
- `main.py`         : Khởi tạo FastAPI, route UI, đọc dữ liệu mẫu, cấu hình server port 8069.
- `routes.py`       : Định nghĩa các endpoint gửi dữ liệu, API tìm kiếm, SSR, AJAX, xuất/gửi dữ liệu, log, health check.
- `models.py`       : Định nghĩa schema dữ liệu cho từng mã SIMO.
- `db_utils.py`     : Kết nối, truy vấn SQL Server, tìm kiếm tương đối, chuẩn hóa dữ liệu.
- `auth.py`         : Hàm lấy token từ SBV.
- `config.py`       : Cấu hình endpoint, tài khoản, server host/port, lấy từ biến môi trường.
- `launcher.py`     : Script launcher Python với dependency checking và error handling.
- `start_server.bat`: Script Windows batch để khởi động dễ dàng.
- `.env.example`    : Template file cấu hình biến môi trường.
- `templates/`      : Giao diện web (base.html, home.html, data_process.html, data_result_ssr.html, ...), dữ liệu mẫu (sample_data.json).
- `logs/`           : Thư mục chứa log gửi nhận cho từng mã SIMO.

## Hướng dẫn sử dụng

### 1. Cài đặt
- Yêu cầu Python >= 3.8 và pip.
- Cài đặt các thư viện cần thiết:
  ```bash
  pip install -r requirements.txt
  # Hoặc nếu chưa có requirements.txt:
  pip install fastapi uvicorn requests jinja2 pandas openpyxl pyodbc
  ```

### 2. Cấu hình hệ thống
- **Cấu hình kết nối Database và Endpoint**:
  - Tạo file `db_config.py` và `config.py` theo mẫu có sẵn (không commit lên git).
  - Sử dụng biến môi trường hoặc file `.env` để cấu hình thông tin nhạy cảm (server, user, password, endpoint, v.v).
  - Không ghi thông tin thật (user, password, endpoint) vào README.md hoặc source code public.
- **Ví dụ cấu hình biến môi trường (Windows):**
  ```cmd
  set SIMO_DB_SERVER=your_db_server
  set SIMO_DB_NAME=your_db_name
  set SIMO_DB_USER=your_db_user
  set SIMO_DB_PASSWORD=your_db_password
  set SIMO_USERNAME=your_sbv_user
  set SIMO_PASSWORD=your_sbv_pass
  set SIMO_CONSUMER_KEY=your_consumer_key
  set SIMO_CONSUMER_SECRET=your_consumer_secret
  set SIMO_TOKEN_URL=https://.../token
  set SIMO_ENTRYPOINT_URL_001=https://.../upload-bao-cao-danh-sach-tktt-khdn-api
  # ... các biến khác tương tự ...
  ```
- **Hoặc cấu hình qua file `.env`** (khuyến nghị, không commit lên git):
  ```env
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
  # ...
  ```

### 3. Khởi động ứng dụng
- Chạy bằng launcher:
  ```bash
  python launcher.py
  ```
- Hoặc chạy trực tiếp:
  ```bash
  python main.py
  # hoặc
  uvicorn main:app --host 0.0.0.0 --port 8069 --reload
  ```
- Có thể thay đổi port bằng biến môi trường `SIMO_SERVER_PORT`.

### 4. Sử dụng giao diện web
- Truy cập: http://localhost:8069/
- **Trang chủ:** Chọn mã SIMO, nhập hoặc upload file JSON, gửi dữ liệu.
- **Xử lý dữ liệu:** Tìm kiếm, lọc, chọn dòng, xuất JSON, gửi SBV.
- **Chuyển đổi Excel sang JSON:**
  - Vào menu "Chuyển Excel sang JSON".
  - Chọn mã SIMO, upload file Excel mẫu đúng định dạng.
  - Xem và tải kết quả JSON.
- **Tải file Excel mẫu:**
  - Vào menu "Tải file Excel mẫu".
  - Chọn mã SIMO, tải về file mẫu để nhập liệu đúng chuẩn.
- **Kiểm tra log:**
  - Vào menu "Log dữ liệu" để xem lịch sử gửi nhận, lỗi, phản hồi từ SBV.

### 5. Bảo mật
- Không commit các file chứa thông tin nhạy cảm (db_config.py, config.py, .env) lên git.
- Đảm bảo thư mục logs/ chỉ dùng cho kiểm thử, không public dữ liệu thật.
- Khi triển khai thực tế, đổi tất cả mật khẩu, endpoint, khóa truy cập.

### 6. Một số lưu ý khác
- Dữ liệu mẫu và template Excel nằm trong thư mục `templates/`.
- Log gửi nhận lưu tại thư mục `logs/`.
- Khi chuyển đổi Excel sang JSON, cần dùng đúng file mẫu để tránh lỗi định dạng.
- Nếu gặp lỗi kết nối database hoặc endpoint, kiểm tra lại biến môi trường và file cấu hình.

## Thay đổi port nhanh
Để thay đổi port mà không cần chỉnh sửa code:

```bash
# Windows
set SIMO_SERVER_PORT=9000 && python launcher.py

# Linux/Mac  
SIMO_SERVER_PORT=9000 python launcher.py

# Hoặc chỉnh trong file .env
SIMO_SERVER_PORT=9000
```

## Hướng dẫn tạo file kết nối Database và Endpoint

### 1. Kết nối Database SQL Server
- Tạo file `db_config.py` (đã có sẵn mẫu, không commit lên git):
```python
import os
DB_SERVER = os.getenv("SIMO_DB_SERVER", "<Your IP Database Server>")
DB_NAME = os.getenv("SIMO_DB_NAME", "simo")
DB_USER = os.getenv("SIMO_DB_USER", "sa")
DB_PASSWORD = os.getenv("SIMO_DB_PASSWORD", "<Your Database connect passwd sa>")
```
- Tạo file `db_utils.py` để truy vấn:
```python
import pyodbc
from db_config import DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD

def get_connection():
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={DB_SERVER};DATABASE={DB_NAME};UID={DB_USER};PWD={DB_PASSWORD}"
    )
    return pyodbc.connect(conn_str)

def search_tktt_tochuc(**kwargs):
    query = "SELECT * FROM TKTT_TOCHUC WHERE 1=1"
    params = []
    for field, value in kwargs.items():
        if value is not None and value != "":
            query += f" AND LOWER(REPLACE({field}, ' ', '')) LIKE ?"
            params.append(f"%{''.join(value.lower().split())}%")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results
```
- Đảm bảo file `db_config.py` nằm trong `.gitignore` để bảo mật thông tin.

### 2. Kết nối Endpoint SBV
- Tạo file `config.py` (hoặc chỉnh sửa):
```python
import os
USERNAME = os.getenv("SIMO_USERNAME", "<YOUR_USERNAME>")
PASSWORD = os.getenv("SIMO_PASSWORD", "<YOUR_PASSWORD>")
CONSUMER_KEY = os.getenv("SIMO_CONSUMER_KEY", "<YOUR_CONSUMER_KEY>")
CONSUMER_SECRET = os.getenv("SIMO_CONSUMER_SECRET", "<YOUR_CONSUMER_SECRET>")
TOKEN_URL = os.getenv("SIMO_TOKEN_URL", "https://...")
ENTRYPOINT_URL_001 = os.getenv("SIMO_ENTRYPOINT_URL_001", "https://...")
ENTRYPOINT_URL_002 = os.getenv("SIMO_ENTRYPOINT_URL_002", "https://...")
ENTRYPOINT_URL_003 = os.getenv("SIMO_ENTRYPOINT_URL_003", "https://...")
ENTRYPOINT_URL_004 = os.getenv("SIMO_ENTRYPOINT_URL_004", "https://...")
```
- Thông tin endpoint, tài khoản có thể cấu hình qua biến môi trường hoặc sửa trực tiếp file này.

- Đảm bảo file `config.py` nằm trong `.gitignore` để bảo mật thông tin.

## Hướng dẫn tạo cấu trúc bảng TKTT_TOCHUC trong Database SQL Server

### 1. Tạo bảng TKTT_TOCHUC
Sử dụng lệnh SQL sau để tạo bảng và các trường đúng định dạng:

```sql
CREATE TABLE TKTT_TOCHUC (
    Cif NVARCHAR(50),
    TenToChuc NVARCHAR(255),
    SoGiayPhepThanhLap NVARCHAR(50),
    LoaiGiayToThanhLapToChuc INT,
    NgayThanhLap NVARCHAR(20),
    DiaChiToChuc NVARCHAR(255),
    HoTenNguoiDaiDien NVARCHAR(100),
    SoGiayToTuyThan NVARCHAR(50),
    LoaiGiayToTuyThan INT,
    NgaySinh NVARCHAR(20),
    GioiTinh INT,
    QuocTich NVARCHAR(50),
    DienThoai NVARCHAR(30),
    SoTaiKhoanToChuc NVARCHAR(50),
    NgayMoTaiKhoan NVARCHAR(20),
    TrangThaiTaiKhoan INT,
    DiaChiMAC NVARCHAR(50),
    SO_IMEI NVARCHAR(50),
    NghiNgo INT,
    LyDoCapNhat NVARCHAR(255),
    UpdateDate DATETIME
);
```

### 2. Định nghĩa các trường
- **Cif**: Mã định danh tổ chức, kiểu NVARCHAR(50)
- **TenToChuc**: Tên tổ chức, kiểu NVARCHAR(255)
- **SoGiayPhepThanhLap**: Số giấy phép thành lập, kiểu NVARCHAR(50)
- **LoaiGiayToThanhLapToChuc**: Loại giấy tờ thành lập, kiểu INT
- **NgayThanhLap**: Ngày thành lập, kiểu NVARCHAR(20)
- **DiaChiToChuc**: Địa chỉ tổ chức, kiểu NVARCHAR(255)
- **HoTenNguoiDaiDien**: Họ tên người đại diện, kiểu NVARCHAR(100)
- **SoGiayToTuyThan**: Số giấy tờ tùy thân, kiểu NVARCHAR(50)
- **LoaiGiayToTuyThan**: Loại giấy tờ tùy thân, kiểu INT
- **NgaySinh**: Ngày sinh người đại diện, kiểu NVARCHAR(20)
- **GioiTinh**: Giới tính, kiểu INT (1: Nam, 2: Nữ)
- **QuocTich**: Quốc tịch, kiểu NVARCHAR(50)
- **DienThoai**: Số điện thoại, kiểu NVARCHAR(30)
- **SoTaiKhoanToChuc**: Số tài khoản tổ chức, kiểu NVARCHAR(50)
- **NgayMoTaiKhoan**: Ngày mở tài khoản, kiểu NVARCHAR(20)
- **TrangThaiTaiKhoan**: Trạng thái tài khoản, kiểu INT
- **DiaChiMAC**: Địa chỉ MAC, kiểu NVARCHAR(50)
- **SO_IMEI**: Số IMEI, kiểu NVARCHAR(50)
- **NghiNgo**: Cờ nghi ngờ, kiểu INT
- **LyDoCapNhat**: Lý do cập nhật, kiểu NVARCHAR(255)
- **UpdateDate**: Ngày cập nhật, kiểu DATETIME

### 3. Lưu ý bảo mật
- **Không lưu thông tin tài khoản, mật khẩu, endpoint thật trong file README hoặc source code.**
- Thông tin kết nối database và endpoint chỉ nên cấu hình qua biến môi trường hoặc file cấu hình riêng, đã được hướng dẫn ở trên.

## API Reference
- Các endpoint `/simo_001/`, `/simo_002/`, `/simo_003/`, `/simo_004/` nhận payload đúng schema, gửi dữ liệu lên SBV.
- API `/data/tktt_tochuc` hỗ trợ tìm kiếm tương đối, không phân biệt hoa thường, bỏ khoảng trắng, trả về JSON.
- API `/data/export-json` và `/data/send-sbv` nhận danh sách dòng và mã simo, xuất JSON đúng schema hoặc gửi lên endpoint tương ứng.

## Lưu ý
- Ứng dụng chỉ phục vụ kiểm thử, nhập liệu, không thay thế hệ thống chính thức.
- Đảm bảo bảo mật thông tin tài khoản, endpoint khi triển khai thực tế.
- Nếu trường dữ liệu int bị None sẽ được tự động chuyển thành 0 khi xuất/gửi dữ liệu.
- Nếu truy vấn trả về datetime sẽ tự động chuyển thành chuỗi ISO để tránh lỗi khi render.

---
Mọi thắc mắc hoặc góp ý, vui lòng liên hệ đội phát triển.