import os
USERNAME = os.getenv("TKTT_USERNAME", "simo-busanhcm")
PASSWORD = os.getenv("TKTT_PASSWORD", "simo660")
CONSUMER_KEY = os.getenv("TKTT_CONSUMER_KEY", "V2sF9dfIfbqXAkBfyauNz9WTJQoa")
CONSUMER_SECRET = os.getenv("TKTT_CONSUMER_SECRET", "lnr90QpFPfClcm1chY5wijrLH08a")
TOKEN_URL = os.getenv("TKTT_TOKEN_URL", "https://mgsimotest.sbv.gov.vn/token")
ENTRYPOINT_URL_001 = os.getenv("TKTT_ENTRYPOINT_URL_001", "https://mgsimotest.sbv.gov.vn/simo/tktt/1.0/upload-bao-cao-danh-sach-tktt-api")
ENTRYPOINT_URL_002 = os.getenv("TKTT_ENTRYPOINT_URL_002", "https://mgsimotest.sbv.gov.vn/simo/tktt/1.0/upload-bao-cao-tktt-nghi-ngo-gian-lan-api")
ENTRYPOINT_URL_003 = os.getenv("TKTT_ENTRYPOINT_URL_003", "https://mgsimotest.sbv.gov.vn/simo/tktt/1.0/upload-bao-cao-cap-nhat-tktt-nghi-ngo-gian-lan-api")
ENTRYPOINT_URL_004 = os.getenv("TKTT_ENTRYPOINT_URL_004", "https://mgsimotest.sbv.gov.vn/simo/tktt/1.0/upload-bao-cao-cap-nhat-khach-hang-mo-tktt-api")

# Server configuration
SERVER_HOST = os.getenv("TKTT_SERVER_HOST", "0.0.0.0")
SERVER_PORT = int(os.getenv("TKTT_SERVER_PORT", "8069"))
DEBUG_MODE = os.getenv("TKTT_DEBUG", "True").lower() == "true"
