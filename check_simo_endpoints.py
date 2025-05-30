import requests

TKTT_ENDPOINTS = {
    "001": "https://mgsimotest.sbv.gov.vn/simo/tktt/1.0/upload-bao-cao-danh-sach-tktt-api",
    "002": "https://mgsimotest.sbv.gov.vn/simo/tktt/1.0/upload-bao-cao-tktt-nghi-ngo-gian-lan-api",
    "003": "https://mgsimotest.sbv.gov.vn/simo/tktt/1.0/upload-bao-cao-cap-nhat-tktt-nghi-ngo-gian-lan-api",
    "004": "https://mgsimotest.sbv.gov.vn/simo/tktt/1.0/upload-bao-cao-cap-nhat-khach-hang-mo-tktt-api",
}

def check_url(url):
    try:
        resp = requests.options(url, timeout=10)
        code = resp.status_code
        if code in [200, 401, 403, 405]:
            return f"Tồn tại (status {code})"
        elif code == 404:
            return "Không tồn tại (404)"
        else:
            return f"Kết quả khác: {code}"
    except Exception as e:
        return f"Lỗi kết nối: {e}"

def main():
    for tktt, url in TKTT_ENDPOINTS.items():
        result = check_url(url)
        print(f"TKTT {tktt}: {url}\n  => {result}\n")

if __name__ == "__main__":
    main()
