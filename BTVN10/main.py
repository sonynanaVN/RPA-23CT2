import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from email_sender import send_violation_email
from config import WEBSITE_URL, WAIT_TIMEOUT


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


def doc_danh_sach_bien_so(file_path):
    try:
        df = pd.read_excel(file_path, header=0)
        bien_so_list = df.iloc[:, 0].dropna().astype(str).str.strip().tolist()
        print(f"✅ Đọc được {len(bien_so_list)} biển số từ file: {file_path}")
        return bien_so_list
    except FileNotFoundError:
        print(f"❌ Không tìm thấy file: {file_path}")
        return []
    except Exception as e:
        print(f"❌ Lỗi đọc file Excel: {e}")
        return []


def kiem_tra_phat_nguoi(driver, bien_so):
    ket_qua = {"bien_so": bien_so, "co_vi_pham": False, "chi_tiet": []}

    try:
        print(f"\n{'='*50}")
        print(f"🔍 Đang kiểm tra biển số: {bien_so}")

        driver.get(WEBSITE_URL)
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text'], input[type='search']")))
        time.sleep(1)

        try:
            radios = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
            chon_duoc = False
            for radio in radios:
                label_text = ""
                label_id = radio.get_attribute("id") or ""
                if label_id:
                    try:
                        lbl = driver.find_element(By.CSS_SELECTOR, f"label[for='{label_id}']")
                        label_text = lbl.text.lower()
                    except:
                        pass
                val = (radio.get_attribute("value") or "").lower()
                if ("ô tô" in label_text or "o to" in label_text) and "điện" not in label_text:
                    driver.execute_script("arguments[0].click();", radio)
                    chon_duoc = True
                    print("  ✅ Đã chọn loại xe: Ô Tô")
                    break
                elif val in ["1", "oto", "o_to", "car"]:
                    driver.execute_script("arguments[0].click();", radio)
                    chon_duoc = True
                    print("  ✅ Đã chọn loại xe: Ô Tô (theo value)")
                    break
            if not chon_duoc and radios:
                driver.execute_script("arguments[0].click();", radios[0])
                print("  ✅ Đã chọn radio đầu tiên (Ô Tô)")
        except Exception as e:
            print(f"  ⚠️  Lỗi chọn loại xe: {e}")

        time.sleep(0.5)

        input_bien_so = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
            "input[type='text'], input[type='search'], input[placeholder*='biển số'], input[placeholder*='19A']"
        )))
        input_bien_so.click()
        input_bien_so.clear()
        time.sleep(0.3)
        input_bien_so.send_keys(bien_so)
        print(f"  ✅ Đã nhập biển số: {bien_so}")
        time.sleep(0.5)

        try:
            btn = wait.until(EC.element_to_be_clickable((By.XPATH,
                "//button[contains(text(),'KIỂM TRA')] | //button[@type='submit'] | //input[@type='submit']"
            )))
        except TimeoutException:
            buttons = driver.find_elements(By.TAG_NAME, "button")
            btn = buttons[0] if buttons else None

        if btn:
            driver.execute_script("arguments[0].click();", btn)
            print("  ✅ Đã click nút KIỂM TRA PHẠT NGUỘI")
        else:
            print("  ❌ Không tìm thấy nút kiểm tra")
            return ket_qua

        time.sleep(4)

        page_lower = driver.page_source.lower()

        khong_vp_keywords = ["không tìm thấy vi phạm", "không có vi phạm", "khong tim thay", "không tìm thấy thông tin"]
        if any(kw in page_lower for kw in khong_vp_keywords):
            print(f"  ✅ Kết quả: KHÔNG CÓ VI PHẠM")
            return ket_qua

        tables = driver.find_elements(By.TAG_NAME, "table")
        for table in tables:
            rows = table.find_elements(By.TAG_NAME, "tr")
            for row in rows[1:]:
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) >= 2:
                    cell_texts = [c.text.strip() for c in cells]
                    if not any(cell_texts):
                        continue
                    ket_qua["chi_tiet"].append({
                        "thoi_gian": cell_texts[0] if len(cell_texts) > 0 else "N/A",
                        "dia_diem":  cell_texts[1] if len(cell_texts) > 1 else "N/A",
                        "loi":       cell_texts[2] if len(cell_texts) > 2 else "N/A",
                        "so_tien":   cell_texts[3] if len(cell_texts) > 3 else "N/A",
                    })

        if ket_qua["chi_tiet"]:
            ket_qua["co_vi_pham"] = True
            print(f"  ⚠️  Kết quả: CÓ VI PHẠM ({len(ket_qua['chi_tiet'])} lỗi)")
        elif any(kw in page_lower for kw in ["vi phạm", "phạt nguội"]):
            ket_qua["co_vi_pham"] = True
            ket_qua["chi_tiet"].append({
                "thoi_gian": "Xem trực tiếp trên website",
                "dia_diem":  "N/A",
                "loi":       "Có vi phạm (vào website xem chi tiết)",
                "so_tien":   "N/A",
            })
            print(f"  ⚠️  Kết quả: CÓ VI PHẠM")
        else:
            print(f"  ✅ Kết quả: KHÔNG CÓ VI PHẠM")

    except TimeoutException:
        print(f"  ❌ Timeout — trang load quá chậm hoặc không tìm thấy phần tử")
    except Exception as e:
        print(f"  ❌ Lỗi: {e}")

    return ket_qua


def main():
    print("=" * 60)
    print("   🤖 RPA BOT: KIỂM TRA PHẠT NGUỘI & GỬI EMAIL")
    print("=" * 60)

    danh_sach = doc_danh_sach_bien_so("bien_so.xlsx")
    if not danh_sach:
        print("❌ Không có biển số để kiểm tra. Dừng chương trình.")
        return

    driver = setup_driver()
    ket_qua_tong = []

    try:
        for bien_so in danh_sach:
            bien_so = bien_so.strip()
            if not bien_so:
                continue
            ket_qua = kiem_tra_phat_nguoi(driver, bien_so)
            ket_qua_tong.append(ket_qua)

            if ket_qua["co_vi_pham"]:
                print(f"\n📧 Phát hiện vi phạm → Đang gửi email...")
                ok = send_violation_email(bien_so=ket_qua["bien_so"], chi_tiet_vi_pham=ket_qua["chi_tiet"])
                print(f"  {'✅ Email gửi thành công!' if ok else '❌ Gửi email thất bại!'}")
            else:
                print(f"  ℹ️  {bien_so}: Không vi phạm → Không gửi email")

            time.sleep(2)
    finally:
        driver.quit()
        print("\n🔒 Đã đóng trình duyệt")

    co_vp = [k for k in ket_qua_tong if k["co_vi_pham"]]
    khong_vp = [k for k in ket_qua_tong if not k["co_vi_pham"]]
    print("\n" + "=" * 60)
    print("   📊 TỔNG KẾT")
    print("=" * 60)
    print(f"Tổng kiểm tra   : {len(ket_qua_tong)}")
    print(f"✅ Không vi phạm: {len(khong_vp)}")
    print(f"⚠️  Có vi phạm   : {len(co_vp)}")
    if co_vp:
        print("\nDanh sách xe vi phạm:")
        for k in co_vp:
            print(f"  🚨 {k['bien_so']}")
    print("=" * 60)


if __name__ == "__main__":
    main()