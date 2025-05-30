import pyodbc
from db_config import DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD

# Hàm chuẩn hóa chuỗi cho tìm kiếm tương đối (không phân biệt hoa thường, loại bỏ khoảng trắng thừa)
def normalize_str(s):
    if s is None:
        return None
    return ''.join(s.lower().split())

def get_connection():
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={DB_SERVER};DATABASE={DB_NAME};UID={DB_USER};PWD={DB_PASSWORD}"
    )
    return pyodbc.connect(conn_str)

def search_tktt_canhan(**kwargs):
    """Tìm kiếm thông tin tài khoản thanh toán khách hàng cá nhân (SIMO 001)"""
    query = "SELECT * FROM TKTT WHERE 1=1"
    params = []
    for field, value in kwargs.items():
        if value is not None and value != "":
            # Tìm kiếm tương đối: loại bỏ khoảng trắng, không phân biệt hoa thường
            query += f" AND LOWER(REPLACE({field}, ' ', '')) LIKE ?"
            params.append(f"%{normalize_str(value)}%")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

def search_tktt_fraud(**kwargs):
    """Tìm kiếm tài khoản nghi ngờ gian lận (SIMO 002)"""
    query = "SELECT * FROM TKTT WHERE 1=1"
    params = []
    for field, value in kwargs.items():
        if value is not None and value != "":
            if field in ['NghiNgo', 'TrangThaiHoatDongTaiKhoan']:
                # Tìm kiếm chính xác cho các trường số
                query += f" AND {field} = ?"
                params.append(value)
            else:
                # Tìm kiếm tương đối cho các trường text
                query += f" AND LOWER(REPLACE({field}, ' ', '')) LIKE ?"
                params.append(f"%{normalize_str(value)}%")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

def search_tktt_fraud_update(**kwargs):
    """Tìm kiếm cập nhật tài khoản nghi ngờ gian lận (SIMO 003)"""
    query = "SELECT * FROM TKTT WHERE 1=1"
    params = []
    for field, value in kwargs.items():
        if value is not None and value != "":
            if field in ['NghiNgo', 'TrangThaiHoatDongTaiKhoan']:
                # Tìm kiếm chính xác cho các trường số
                query += f" AND {field} = ?"
                params.append(value)
            else:
                # Tìm kiếm tương đối cho các trường text
                query += f" AND LOWER(REPLACE({field}, ' ', '')) LIKE ?"
                params.append(f"%{normalize_str(value)}%")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

def search_tktt_customer_update(**kwargs):
    """Tìm kiếm cập nhật khách hàng mở TKTT (SIMO 004)"""
    query = "SELECT * FROM TKTT WHERE 1=1"
    params = []
    for field, value in kwargs.items():
        if value is not None and value != "":
            if field in ['LoaiD', 'GioiTinh', 'LoaiTaiKhoan', 'TrangThaiHoatDongTaiKhoan', 'PhuongThucMoTaiKhoan']:
                # Tìm kiếm chính xác cho các trường số
                query += f" AND {field} = ?"
                params.append(value)
            else:
                # Tìm kiếm tương đối cho các trường text
                query += f" AND LOWER(REPLACE({field}, ' ', '')) LIKE ?"
                params.append(f"%{normalize_str(value)}%")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

# Giữ lại function cũ cho tương thích ngược
def search_tktt_tochuc(**kwargs):
    """Tìm kiếm thông tin tài khoản thanh toán tổ chức (legacy)"""
    query = "SELECT * FROM TKTT WHERE 1=1"
    params = []
    for field, value in kwargs.items():
        if value is not None and value != "":
            # Tìm kiếm tương đối: loại bỏ khoảng trắng, không phân biệt hoa thường
            query += f" AND LOWER(REPLACE({field}, ' ', '')) LIKE ?"
            params.append(f"%{normalize_str(value)}%")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

# Statistics functions cho từng loại SIMO
def get_stats_canhan():
    """Thống kê cho TKTT cá nhân (SIMO 001)"""
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Tổng số khách hàng
        cursor.execute("SELECT COUNT(DISTINCT Cif) as total FROM TKTT")
        total_customers = cursor.fetchone()[0]
        
        # Thống kê theo trạng thái
        cursor.execute("SELECT TrangThaiHoatDongTaiKhoan, COUNT(*) as count FROM TKTT GROUP BY TrangThaiHoatDongTaiKhoan")
        status_stats = {str(row[0]): row[1] for row in cursor.fetchall()}
        
        # Thống kê theo năm sinh
        cursor.execute("SELECT YEAR(CONVERT(date, NgaySinh, 103)) as year, COUNT(*) as count FROM TKTT GROUP BY YEAR(CONVERT(date, NgaySinh, 103)) ORDER BY year")
        birth_year_stats = {str(row[0]): row[1] for row in cursor.fetchall()}
        
        # Thống kê theo năm mở tài khoản
        cursor.execute("SELECT YEAR(CONVERT(date, NgayMoTaiKhoan, 103)) as year, COUNT(*) as count FROM TKTT GROUP BY YEAR(CONVERT(date, NgayMoTaiKhoan, 103)) ORDER BY year")
        open_year_stats = {str(row[0]): row[1] for row in cursor.fetchall()}
        
        # Top 10 khách hàng có nhiều tài khoản nhất
        cursor.execute("SELECT TOP 10 Cif, TenKhachHang, COUNT(*) as count FROM TKTT GROUP BY Cif, TenKhachHang ORDER BY count DESC")
        top_customers = [{"Cif": row[0], "TenKhachHang": row[1], "count": row[2]} for row in cursor.fetchall()]
        
        # 10 tài khoản được mở gần nhất
        cursor.execute("SELECT TOP 10 Cif, TenKhachHang, SoTaiKhoan, NgayMoTaiKhoan FROM TKTT ORDER BY CONVERT(date, NgayMoTaiKhoan, 103) DESC")
        latest_accounts = [{"Cif": row[0], "TenKhachHang": row[1], "SoTaiKhoan": row[2], "NgayMoTaiKhoan": row[3]} for row in cursor.fetchall()]
        
        # Status labels
        status_labels = {
            "1": "Hoạt động",
            "2": "Tạm ngừng dịch vụ", 
            "3": "Tạm khóa",
            "4": "Phong tỏa",
            "5": "Đã đóng",
            "6": "Xóa"
        }
        
        return {
            "total_customers": total_customers,
            "status": status_stats,
            "status_labels": status_labels,
            "birth_year": birth_year_stats,
            "open_year": open_year_stats,
            "top_customers": top_customers,
            "latest_accounts": latest_accounts
        }

def get_stats_fraud():
    """Thống kê cho tài khoản nghi ngờ gian lận (SIMO 002)"""
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Thống kê số lượng theo từng loại nghi ngờ
        cursor.execute("SELECT NghiNgo, COUNT(*) as count FROM TKTT GROUP BY NghiNgo ORDER BY NghiNgo")
        fraud_stats_raw = cursor.fetchall()
        
        # Mapping mã nghi ngờ với mô tả
        fraud_labels = {
            0: "Không nghi ngờ",
            1: "Thông tin không khớp CSDL quốc gia",
            2: "TK được quảng cáo/mua bán online",
            3: "Nhận tiền từ nhiều TK rồi rút ngay",
            4: "Có >03 giao dịch từ TK nghi ngờ lừa đảo",
            5: "KH thuộc danh sách cảnh báo của NHNN/Công an",
            6: "Giao dịch bất thường",
            7: "Cùng MAC dùng cho >01 TK",
            8: "Dấu hiệu khác"
        }
        
        fraud_stats = {}
        for row in fraud_stats_raw:
            code = row[0]
            count = row[1]
            label = fraud_labels.get(code, f"Mã {code}")
            fraud_stats[f"Mã {code}: {label}"] = count
        
        # Danh sách tài khoản nghi ngờ (top 50)
        cursor.execute("SELECT TOP 50 Cif, TenKhachHang, SoTaiKhoan, NghiNgo, GhiChu FROM TKTT WHERE NghiNgo > 0 ORDER BY NghiNgo")
        fraud_accounts = []
        for row in cursor.fetchall():
            fraud_accounts.append({
                "Cif": row[0],
                "TenKhachHang": row[1], 
                "SoTaiKhoan": row[2],
                "NghiNgo": row[3],
                "NghiNgoReason": fraud_labels.get(row[3], f"Mã {row[3]}")
            })
        
        return {
            "fraud_stats": fraud_stats,
            "fraud_accounts": fraud_accounts
        }

def search_tktt_nghi_ngo(
    Cif=None,
    SoTaiKhoan=None,
    TenKhachHang=None,
    TrangThaiHoatDongTaiKhoan=None,
    NghiNgo=None,
    GhiChu=None
):
    """
    Tìm kiếm dữ liệu TKTT nghi ngờ gian lận (SIMO 002)
    """
    conn = get_connection()
    try:
        cursor = conn.cursor()
        conditions = []
        params = []
        
        if Cif:
            conditions.append("Cif LIKE ?")
            params.append(f"%{Cif}%")
        if SoTaiKhoan:
            conditions.append("SoTaiKhoan LIKE ?")
            params.append(f"%{SoTaiKhoan}%")
        if TenKhachHang:
            conditions.append("TenKhachHang LIKE ?")
            params.append(f"%{TenKhachHang}%")
        if TrangThaiHoatDongTaiKhoan is not None:
            conditions.append("TrangThaiHoatDongTaiKhoan = ?")
            params.append(TrangThaiHoatDongTaiKhoan)
        if NghiNgo is not None:
            conditions.append("NghiNgo = ?")
            params.append(NghiNgo)
        if GhiChu:
            conditions.append("GhiChu LIKE ?")
            params.append(f"%{GhiChu}%")
        
        where_clause = " WHERE " + " AND ".join(conditions) if conditions else ""
        query = f"""
        SELECT Cif, SoTaiKhoan, TenKhachHang, TrangThaiHoatDongTaiKhoan, 
               NghiNgo, GhiChu
        FROM TKTT
        {where_clause}
        ORDER BY TenKhachHang
        """
        
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results
    except Exception as e:
        print(f"Lỗi tìm kiếm TKTT nghi ngờ: {e}")
        return []
    finally:
        conn.close()

def search_tktt_cap_nhat_nghi_ngo(
    Cif=None,
    TenKhachHang=None,
    SoTaiKhoan=None,
    TrangThaiHoatDongTaiKhoan=None,
    NghiNgo=None,
    GhiChu=None,
    LyDoCapNhat=None
):
    """
    Tìm kiếm dữ liệu TKTT cập nhật nghi ngờ gian lận (SIMO 003)
    """
    conn = get_connection()
    try:
        cursor = conn.cursor()
        conditions = []
        params = []
        
        if Cif:
            conditions.append("Cif LIKE ?")
            params.append(f"%{Cif}%")
        if TenKhachHang:
            conditions.append("TenKhachHang LIKE ?")
            params.append(f"%{TenKhachHang}%")
        if SoTaiKhoan:
            conditions.append("SoTaiKhoan LIKE ?")
            params.append(f"%{SoTaiKhoan}%")
        if TrangThaiHoatDongTaiKhoan is not None:
            conditions.append("TrangThaiHoatDongTaiKhoan = ?")
            params.append(TrangThaiHoatDongTaiKhoan)
        if NghiNgo is not None:
            conditions.append("NghiNgo = ?")
            params.append(NghiNgo)
        if GhiChu:
            conditions.append("GhiChu LIKE ?")
            params.append(f"%{GhiChu}%")
        if LyDoCapNhat:
            conditions.append("LyDoCapNhat LIKE ?")
            params.append(f"%{LyDoCapNhat}%")
        
        where_clause = " WHERE " + " AND ".join(conditions) if conditions else ""
        query = f"""
        SELECT Cif, TenKhachHang, SoTaiKhoan, TrangThaiHoatDongTaiKhoan, 
               NghiNgo, GhiChu, LyDoCapNhat
        FROM TKTT
        {where_clause}
        ORDER BY TenKhachHang
        """
        
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results
    except Exception as e:
        print(f"Lỗi tìm kiếm TKTT cập nhật nghi ngờ: {e}")
        return []
    finally:
        conn.close()

def search_tktt_cap_nhat_kh(
    Cif=None,
    SoId=None,
    LoaiD=None,
    TenKhachHang=None,
    NgaySinh=None,
    GioiTinh=None,
    MaSoThue=None,
    SoDienThoaiDangKyDichVu=None,
    DiaChi=None,
    DiaChiKiemSoatTruyCap=None,
    MaSoNhanDangThietBiDiDong=None,
    SoTaiKhoan=None,
    TrangThaiHoatDongTaiKhoan=None,
    NgayXacThucTaiQuay=None,
    LoaiTaiKhoan=None,
    NgayMoTaiKhoan=None,
    PhuongThucMoTaiKhoan=None,
    GhiChu=None,
    QuocTich=None
):
    """
    Tìm kiếm dữ liệu TKTT cập nhật khách hàng mở TKTT (SIMO 004)
    """
    conn = get_connection()
    try:
        cursor = conn.cursor()
        conditions = []
        params = []
        
        # Tìm kiếm tương đối cho các trường text
        text_fields = {
            'Cif': Cif,
            'SoId': SoId,
            'TenKhachHang': TenKhachHang,
            'NgaySinh': NgaySinh,
            'MaSoThue': MaSoThue,
            'SoDienThoaiDangKyDichVu': SoDienThoaiDangKyDichVu,
            'DiaChi': DiaChi,
            'DiaChiKiemSoatTruyCap': DiaChiKiemSoatTruyCap,
            'MaSoNhanDangThietBiDiDong': MaSoNhanDangThietBiDiDong,
            'SoTaiKhoan': SoTaiKhoan,
            'NgayXacThucTaiQuay': NgayXacThucTaiQuay,
            'NgayMoTaiKhoan': NgayMoTaiKhoan,
            'GhiChu': GhiChu,
            'QuocTich': QuocTich
        }
        
        for field, value in text_fields.items():
            if value:
                conditions.append(f"{field} LIKE ?")
                params.append(f"%{value}%")
        
        # Tìm kiếm chính xác cho các trường số
        numeric_fields = {
            'LoaiD': LoaiD,
            'GioiTinh': GioiTinh,
            'TrangThaiHoatDongTaiKhoan': TrangThaiHoatDongTaiKhoan,
            'LoaiTaiKhoan': LoaiTaiKhoan,
            'PhuongThucMoTaiKhoan': PhuongThucMoTaiKhoan
        }
        
        for field, value in numeric_fields.items():
            if value is not None:
                conditions.append(f"{field} = ?")
                params.append(value)
        
        where_clause = " WHERE " + " AND ".join(conditions) if conditions else ""
        query = f"""
        SELECT Cif, SoId, LoaiD, TenKhachHang, NgaySinh, GioiTinh, MaSoThue,
               SoDienThoaiDangKyDichVu, DiaChi, DiaChiKiemSoatTruyCap,
               MaSoNhanDangThietBiDiDong, SoTaiKhoan, TrangThaiHoatDongTaiKhoan,
               NgayXacThucTaiQuay, LoaiTaiKhoan, NgayMoTaiKhoan,
               PhuongThucMoTaiKhoan, GhiChu, QuocTich
        FROM TKTT
        {where_clause}
        ORDER BY TenKhachHang
        """
        
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results
    except Exception as e:
        print(f"Lỗi tìm kiếm TKTT cập nhật khách hàng: {e}")
        return []
    finally:
        conn.close()
