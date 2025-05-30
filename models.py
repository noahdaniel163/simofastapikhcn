from pydantic import BaseModel
from typing import Optional

class Simo001Payload(BaseModel):
    """Dịch vụ thu thập danh sách TKTT khách hàng cá nhân định kỳ (simo_001)"""
    Cif: str  # Mã số khách hàng (36 ký tự)
    SoId: str  # Số ID (15 ký tự)
    LoaiD: int  # Loại ID (1: CCCD, 2: Thẻ căn cước,...)
    TenKhachHang: str  # Tên khách hàng (150 ký tự)
    NgaySinh: str  # Ngày sinh (dd/MM/YYYY)
    GioiTinh: int  # Giới tính (0: Nữ, 1: Nam, 2: Khác)
    MaSoThue: Optional[str] = None  # Mã số thuế (10 hoặc 13 ký tự, không bắt buộc)
    SoDienThoaiDangKyDichVu: str  # Số điện thoại Mobile Banking
    DiaChi: Optional[str] = None  # Địa chỉ thường trú (300 ký tự, không bắt buộc)
    DiaChiKiemSoatTruyCap: str  # Địa chỉ MAC của thiết bị Mobile Banking
    MaSoNhanDangThietBiDong: Optional[str] = None  # IMEI (không bắt buộc)
    SoTaiKhoan: str  # Số tài khoản (36 ký tự)
    LoaiTaiKhoan: Optional[int] = None  # Loại tài khoản (1: VND, 2: Ngoại tệ, không bắt buộc)
    TrangThaiHoatDongTaiKhoan: int  # Trạng thái tài khoản (1: Hoạt động, 2: Tạm ngừng,...)
    NgayMoTaiKhoan: str  # Ngày mở tài khoản (dd/MM/YYYY)
    PhuongThucMoTaiKhoan: Optional[int] = None  # Phương thức mở (1: Tại quầy, 2: eKYC, không bắt buộc)
    NgayXacThucTaiQuay: Optional[str] = None  # Ngày xác thực tại quầy (không bắt buộc)
    QuocTich: str  # Quốc tịch (36 ký tự)

class Simo002Payload(BaseModel):
    """TKTT nghi ngờ gian lận (simo_002)"""
    Cif: str  # Mã số khách hàng (36 ký tự)
    SoTaiKhoan: str  # Số tài khoản (36 ký tự)
    TenKhachHang: str  # Tên khách hàng (150 ký tự)
    TrangThaiHoatDongTaiKhoan: int  # Trạng thái tài khoản (1-5)
    # 1: Đang hoạt động, 2: Tạm ngừng dịch vụ, 3: Tạm khóa, 4: Phong tỏa, 5: Đã đóng
    NghiNgo: int  # Mã nghi ngờ (0-8)
    # 0: Không nghi ngờ, 1: Thông tin không khớp CSDL quốc gia
    # 2: TK được quảng cáo/mua bán online, 3: Nhận tiền từ nhiều TK rồi rút ngay
    # 4: Có >03 giao dịch từ TK nghi ngờ lừa đảo
    # 5: KH thuộc danh sách cảnh báo của NHNN/Công an
    # 6: Giao dịch bất thường, 7: Cùng MAC dùng cho >01 TK
    # 8: Dấu hiệu khác (ghi rõ trong GhiChu)
    GhiChu: str  # Ghi chú (500 ký tự)

class Simo003Payload(BaseModel):
    """Cập nhật TKTT nghi ngờ gian lận (simo_003)"""
    Cif: str  # Mã số khách hàng (36 ký tự)
    TenKhachHang: str  # Tên khách hàng (150 ký tự)
    SoTaiKhoan: str  # Số tài khoản (36 ký tự)
    TrangThaiHoatDongTaiKhoan: int  # Trạng thái tài khoản (1-5)
    NghiNgo: int  # Mã nghi ngờ (0-8)
    GhiChu: str  # Ghi chú (500 ký tự)
    LyDoCapNhat: str  # Lý do cập nhật thông tin (500 ký tự)

class Simo004Payload(BaseModel):
    """Cập nhật khách hàng mở TKTT (simo_004)"""
    Cif: str  # Mã số khách hàng (36 ký tự)
    SoId: str  # Số giấy tờ định danh (15 ký tự)
    LoaiD: int  # Loại ID (1-7)
    # 1: CCCD gắn chip, 2: CCCD mã vạch, 3: CMND, 4: Hộ chiếu
    # 5: Giấy chứng nhận căn cước, 6: Tài khoản định danh & xác thực điện tử, 7: Giấy tờ khác
    TenKhachHang: str  # Tên khách hàng (150 ký tự)
    NgaySinh: str  # Ngày sinh (dd/MM/yyyy)
    GioiTinh: int  # Giới tính (0: Nữ, 1: Nam, 2: Khác)
    MaSoThue: str  # Mã số thuế (10 hoặc 13 ký tự)
    SoDienThoaiDangKyDichVu: str  # SĐT đăng ký Mobile Banking (15 ký tự)
    DiaChi: str  # Địa chỉ thường trú (300 ký tự)
    DiaChiKiemSoatTruyCap: str  # MAC Address thiết bị (60 ký tự)
    MaSoNhanDangThietBiDong: str  # IMEI thiết bị di động (36 ký tự)
    SoTaiKhoan: str  # Số tài khoản (36 ký tự)
    TrangThaiHoatDongTaiKhoan: int  # Trạng thái tài khoản (1-6)
    # 1: Đang hoạt động, 2: Tạm ngừng dịch vụ, 3: Tạm khóa
    # 4: Phong tỏa, 5: Đã đóng, 6: Xóa
    NgayXacThucTaiQuay: str  # Ngày KH xác thực tại quầy (dd/MM/yyyy)
    LoaiTaiKhoan: int  # Loại tài khoản (1: VNĐ, 2: Ngoại tệ)
    NgayMoTaiKhoan: str  # Ngày mở TK (dd/MM/yyyy)
    PhuongThucMoTaiKhoan: int  # Phương thức mở (1: Mở tại quầy, 2: Mở qua eKYC)
    GhiChu: str  # Ghi chú (500 ký tự)
    QuocTich: str  # Quốc tịch (36 ký tự, ví dụ: "VN")
