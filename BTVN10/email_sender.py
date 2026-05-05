"""
Module gửi email thông báo vi phạm phạt nguội qua Gmail SMTP
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from config import (
    EMAIL_SENDER,
    EMAIL_PASSWORD,
    EMAIL_RECEIVER,
    SMTP_SERVER,
    SMTP_PORT
)


def tao_noi_dung_html(bien_so: str, chi_tiet_vi_pham: list[dict]) -> str:
    """Tạo nội dung email dạng HTML đẹp"""

    # Tạo các dòng bảng chi tiết vi phạm
    rows_html = ""
    for i, vp in enumerate(chi_tiet_vi_pham, 1):
        rows_html += f"""
        <tr style="background-color: {'#fff5f5' if i % 2 == 1 else '#ffffff'};">
            <td style="padding: 10px; border: 1px solid #fca5a5; text-align: center;">{i}</td>
            <td style="padding: 10px; border: 1px solid #fca5a5;">{vp.get('thoi_gian', 'N/A')}</td>
            <td style="padding: 10px; border: 1px solid #fca5a5;">{vp.get('dia_diem', 'N/A')}</td>
            <td style="padding: 10px; border: 1px solid #fca5a5; color: #dc2626; font-weight: bold;">{vp.get('loi', 'N/A')}</td>
            <td style="padding: 10px; border: 1px solid #fca5a5; text-align: right;">{vp.get('so_tien', 'N/A')}</td>
        </tr>
        """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"></head>
    <body style="font-family: Arial, sans-serif; background: #f9fafb; padding: 20px;">
        <div style="max-width: 680px; margin: auto; background: white; border-radius: 12px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1); overflow: hidden;">

            <!-- Header -->
            <div style="background: linear-gradient(135deg, #dc2626, #991b1b);
                        padding: 30px; text-align: center;">
                <div style="font-size: 40px; margin-bottom: 8px;">🚨</div>
                <h1 style="color: white; margin: 0; font-size: 24px; letter-spacing: 1px;">
                    CẢNH BÁO PHẠT NGUỘI
                </h1>
                <p style="color: #fca5a5; margin: 8px 0 0; font-size: 14px;">
                    Phát hiện vi phạm giao thông
                </p>
            </div>

            <!-- Thông tin biển số -->
            <div style="padding: 24px 30px; border-bottom: 2px solid #fee2e2;">
                <table width="100%">
                    <tr>
                        <td>
                            <p style="margin: 0; color: #6b7280; font-size: 13px; text-transform: uppercase;">
                                Biển số xe
                            </p>
                            <p style="margin: 4px 0 0; font-size: 28px; font-weight: bold;
                                      color: #111827; letter-spacing: 2px;">
                                🚗 {bien_so}
                            </p>
                        </td>
                        <td style="text-align: right;">
                            <span style="background: #fee2e2; color: #dc2626; padding: 6px 16px;
                                         border-radius: 999px; font-weight: bold; font-size: 14px;">
                                ⚠️ CÓ VI PHẠM
                            </span>
                        </td>
                    </tr>
                </table>
                <p style="margin: 12px 0 0; color: #6b7280; font-size: 13px;">
                    📅 Thời gian kiểm tra: {datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}
                </p>
            </div>

            <!-- Bảng chi tiết vi phạm -->
            <div style="padding: 24px 30px;">
                <h2 style="margin: 0 0 16px; font-size: 16px; color: #374151;">
                    📋 Chi tiết vi phạm ({len(chi_tiet_vi_pham)} lỗi)
                </h2>
                <table width="100%" style="border-collapse: collapse; font-size: 13px;">
                    <thead>
                        <tr style="background: #dc2626; color: white;">
                            <th style="padding: 10px; border: 1px solid #fca5a5;">#</th>
                            <th style="padding: 10px; border: 1px solid #fca5a5;">Thời gian</th>
                            <th style="padding: 10px; border: 1px solid #fca5a5;">Địa điểm</th>
                            <th style="padding: 10px; border: 1px solid #fca5a5;">Lỗi vi phạm</th>
                            <th style="padding: 10px; border: 1px solid #fca5a5;">Mức phạt</th>
                        </tr>
                    </thead>
                    <tbody>
                        {rows_html}
                    </tbody>
                </table>
            </div>

            <!-- Cảnh báo hành động -->
            <div style="margin: 0 30px 24px; background: #fff7ed; border-left: 4px solid #f97316;
                        border-radius: 4px; padding: 14px 16px;">
                <p style="margin: 0; font-size: 13px; color: #92400e;">
                    <strong>⚡ Lưu ý:</strong> Vui lòng đến cơ quan công an có thẩm quyền để nộp phạt
                    theo đúng quy định. Chậm nộp phạt có thể dẫn đến tạm giữ phương tiện.
                </p>
            </div>

            <!-- Footer -->
            <div style="background: #f9fafb; padding: 16px 30px; text-align: center;
                        border-top: 1px solid #e5e7eb;">
                <p style="margin: 0; font-size: 12px; color: #9ca3af;">
                    Email này được tự động tạo bởi <strong>RPA Bot Kiểm Tra Phạt Nguội</strong><br>
                    Nguồn dữ liệu: <a href="https://www.phatnguoixe.com" style="color: #3b82f6;">
                    phatnguoixe.com</a>
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    return html


def tao_noi_dung_text(bien_so: str, chi_tiet_vi_pham: list[dict]) -> str:
    """Tạo nội dung email dạng text thuần"""
    lines = [
        "=" * 50,
        "   CẢNH BÁO PHẠT NGUỘI",
        "=" * 50,
        f"Biển số   : {bien_so}",
        f"Trạng thái: CÓ VI PHẠM",
        f"Thời gian kiểm tra: {datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}",
        "",
        "Chi tiết vi phạm:",
        "-" * 50,
    ]
    for i, vp in enumerate(chi_tiet_vi_pham, 1):
        lines += [
            f"Vi phạm #{i}:",
            f"  - Thời gian : {vp.get('thoi_gian', 'N/A')}",
            f"  - Địa điểm  : {vp.get('dia_diem', 'N/A')}",
            f"  - Lỗi       : {vp.get('loi', 'N/A')}",
            f"  - Mức phạt  : {vp.get('so_tien', 'N/A')}",
            "",
        ]
    lines += [
        "=" * 50,
        "Email tự động từ RPA Bot Kiểm Tra Phạt Nguội",
        "Nguồn: https://www.phatnguoixe.com",
    ]
    return "\n".join(lines)


def send_violation_email(bien_so: str, chi_tiet_vi_pham: list[dict]) -> bool:
    """
    Gửi email thông báo vi phạm qua Gmail SMTP

    Args:
        bien_so: Biển số xe vi phạm
        chi_tiet_vi_pham: Danh sách dict chứa thông tin vi phạm

    Returns:
        bool: True nếu gửi thành công, False nếu thất bại
    """
    try:
        # Tạo message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"🚨 Cảnh báo phạt nguội - Biển số {bien_so}"
        msg["From"]    = EMAIL_SENDER
        msg["To"]      = EMAIL_RECEIVER

        # Gắn cả 2 phần: text thuần + HTML
        part_text = MIMEText(tao_noi_dung_text(bien_so, chi_tiet_vi_pham), "plain", "utf-8")
        part_html = MIMEText(tao_noi_dung_html(bien_so, chi_tiet_vi_pham), "html",  "utf-8")

        # Email client sẽ ưu tiên hiển thị HTML
        msg.attach(part_text)
        msg.attach(part_html)

        # Kết nối và gửi qua Gmail SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

        return True

    except smtplib.SMTPAuthenticationError:
        print("  ❌ Lỗi xác thực Gmail. Kiểm tra EMAIL và APP PASSWORD trong config.py")
        return False
    except smtplib.SMTPException as e:
        print(f"  ❌ Lỗi SMTP: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Lỗi gửi email: {e}")
        return False