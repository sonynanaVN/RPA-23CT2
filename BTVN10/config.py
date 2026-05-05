"""
Cấu hình cho RPA Bot Kiểm Tra Phạt Nguội
⚠️  QUAN TRỌNG: Điền thông tin của bạn vào đây trước khi chạy!
"""

# ─────────────────────────────────────────────
#  WEBSITE CẦN TRUY CẬP
# ─────────────────────────────────────────────
WEBSITE_URL = "https://www.phatnguoixe.com/"
WAIT_TIMEOUT = 15  # Giây chờ tối đa cho các thao tác Selenium

# ─────────────────────────────────────────────
#  CẤU HÌNH EMAIL (Gmail SMTP)
# ─────────────────────────────────────────────
# ⚡ Bước chuẩn bị tài khoản Gmail:
#   1. Bật xác minh 2 bước: https://myaccount.google.com/security
#   2. Tạo App Password: https://myaccount.google.com/apppasswords
#      → Chọn App: "Mail" / Device: "Other" → đặt tên "RPA Bot"
#      → Copy mật khẩu 16 ký tự được tạo ra (dạng: xxxx xxxx xxxx xxxx)
#   3. Dán vào EMAIL_PASSWORD bên dưới (không cần dấu cách)

EMAIL_SENDER   = "rokhananana98@gmail.com"      # ← Email Gmail của bạn
EMAIL_PASSWORD = "zdvctubzkhivpetz"       # ← App Password 16 ký tự
EMAIL_RECEIVER = "samsamsam0905@gmail.com"  # ← Email nhận thông báo

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT   = 587  # TLS port