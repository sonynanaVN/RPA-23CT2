import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ----------------------------------------
# CẤU HÌNH
# ----------------------------------------
GMAIL_USER     = "rokhananana98@gmail.com"
GMAIL_PASSWORD = "zdvctubzkhivpetz"

# ✅ Danh sách người nhận - thêm email vào đây
SEND_TO_LIST = [
    "quocdat051020@gmail.com",
    
]

SUBJECT = "Lời xin chào từ đội ngũ SonaAI!"
BODY    = """
Xin chào bạn,
 
Hôm nay, khi bạn mở email này, có một điều mình muốn nhắc bạn nhớ:
 
    "Mỗi buổi sáng thức dậy là một tờ giấy trắng.
     Chỉ có bạn mới quyết định được hôm nay sẽ viết gì lên đó."
 
────────────────────────────────────────
 
Có những ngày bạn cảm thấy mọi thứ quá nặng nề.
Công việc chồng chất. Mục tiêu còn xa. Động lực dường như biến mất.
 
Nhưng hãy nhớ —
 
Không ai đi từ điểm A đến điểm Z trong một bước.
Người thành công không phải người không bao giờ vấp ngã,
mà là người chọn đứng dậy thêm một lần nữa.
 
────────────────────────────────────────
 
🔥 3 điều hãy làm ngay hôm nay:
 
  1. Làm một việc nhỏ mà bạn đã trì hoãn quá lâu.
  2. Nói lời cảm ơn với một người quan trọng trong cuộc đời bạn.
  3. Dành 10 phút yên tĩnh — chỉ để thở và tin tưởng vào bản thân.
 
────────────────────────────────────────
 
Bạn có nhiều tiềm năng hơn bạn nghĩ.
Hành trình của bạn chưa kết thúc — thực ra, phần hay nhất vẫn còn ở phía trước.
 
Chúc bạn một ngày tràn đầy năng lượng và ý nghĩa. 💪
gitty gitty
Trân trọng,
Team Sona 🚀
"""

# ----------------------------------------
# HÀM GỬI EMAIL
# ----------------------------------------
def send_email(to, subject, body):
    msg = MIMEMultipart()
    msg["From"]    = GMAIL_USER
    msg["To"]      = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.sendmail(GMAIL_USER, to, msg.as_string())
        print(f"✅ Gửi thành công → {to}")
        return True

    except smtplib.SMTPAuthenticationError:
        print("❌ Lỗi xác thực! Kiểm tra lại Gmail và App Password.")
        return False
    except smtplib.SMTPException as e:
        print(f"❌ Lỗi SMTP [{to}]: {e}")
        return False
    except Exception as e:
        print(f"❌ Lỗi không xác định [{to}]: {e}")
        return False

# ----------------------------------------
# MAIN - Gửi cho nhiều người
# ----------------------------------------
if __name__ == "__main__":
    total   = len(SEND_TO_LIST)
    success = 0
    failed  = 0

    print(f"\n📧 Bắt đầu gửi email cho {total} người...\n")

    for i, email in enumerate(SEND_TO_LIST, 1):
        print(f"[{i}/{total}] Đang gửi → {email}")
        ok = send_email(email, SUBJECT, BODY)

        if ok:
            success += 1
        else:
            failed += 1

        # Chờ 2 giây giữa mỗi email để tránh bị Gmail chặn spam
        if i < total:
            time.sleep(2)

    print(f"\n{'='*40}")
    print(f"  ✅ Thành công : {success}")
    print(f"  ❌ Thất bại   : {failed}")
    print(f"  📊 Tổng       : {total}")
    print(f"{'='*40}\n")