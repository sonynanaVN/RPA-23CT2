import smtplib
import time
from email.mime.text import MIMEText
#1Y3GY6GSUN23WUTCZM5NUYZV
sender = "rokhananana98@gmail.com"
password = "zdvctubzkhivpetz"

receivers = [

    "khangle.230905@gmail.com"
]

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)

for r in receivers:
    body = f"""Kính gửi Anh/Chị,

Tôi xin chân thành cảm ơn Anh/Chị đã tham gia và phối hợp trong quá trình thực hiện đề tài nghiên cứu khoa học.

Sự hỗ trợ và đóng góp của Anh/Chị là vô cùng quý báu, góp phần quan trọng vào kết quả của đề tài.

Kính chúc Anh/Chị sức khỏe, thành công trong công việc và cuộc sống.

Trân trọng,
Thành viên nghiên cứu - Anh
"""
    
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = "Thư cảm ơn tham gia đề tài NCKH"
    msg["From"] = sender
    msg["To"] = r

    try:
        server.sendmail(sender, r, msg.as_string())
        print(f"✅ Đã gửi tới {r}")
    except Exception as e:
        print(f"❌ Lỗi gửi tới {r}: {e}")
    
    time.sleep(3)  # tránh spam

server.quit()
print("🎉 Gửi xong!")