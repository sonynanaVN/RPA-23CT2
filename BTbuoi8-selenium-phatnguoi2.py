from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
import re

def get_edge_version():
    """Tự động lấy version Edge đang cài"""
    try:
        result = subprocess.run(
            ['reg', 'query', r'HKEY_CURRENT_USER\Software\Microsoft\Edge\BLBeacon', '/v', 'version'],
            capture_output=True, text=True
        )
        version = re.search(r'\d+\.\d+\.\d+\.\d+', result.stdout)
        return version.group() if version else None
    except:
        return None

def tao_driver():
    options = Options()

    # Ẩn dấu hiệu bot
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    # ✅ Edge tự tìm driver có sẵn trong hệ thống — không cần cài thêm!
    driver = webdriver.Edge(options=options)

    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    return driver

def tra_cuu_phat_nguoi(driver, bien_so):
    try:
        print(f"\n🔍 Đang tra cứu: {bien_so} ...")
        driver.get("https://phatnguoi.com/")
        time.sleep(3)

        # Nhập biển số
        input_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "BienKiemSoat"))
        )
        input_box.clear()
        input_box.send_keys(bien_so)
        time.sleep(1)

        # Click nút tra cứu
        btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        btn.click()
        time.sleep(4)

        print("\n" + "=" * 50)
        print(f"   KẾT QUẢ BIỂN SỐ: {bien_so}")
        print("=" * 50)

        try:
            # Thử tìm bảng kết quả
            results = driver.find_elements(By.XPATH, "//table//tr")
            if results:
                for row in results:
                    text = row.text.strip()
                    if text:
                        print(text)
            else:
                # In toàn bộ nội dung
                body = driver.find_element(By.TAG_NAME, "body")
                lines = body.text.strip().split("\n")
                for line in lines:
                    if line.strip():
                        print(line.strip())

        except Exception as e:
            print(f"Không tìm thấy kết quả: {e}")

        print("=" * 50)

    except Exception as e:
        print(f"❌ Lỗi: {e}")

# ===== CHƯƠNG TRÌNH CHÍNH =====
if __name__ == "__main__":
    print("=" * 50)
    print("   TRA CỨU PHẠT NGUỘI BIỂN SỐ XE")
    print("   Nguồn: phatnguoi.com")
    print("=" * 50)

    edge_ver = get_edge_version()
    if edge_ver:
        print(f"✅ Phát hiện Edge version: {edge_ver}")

    driver = tao_driver()

    try:
        while True:
            bien_so = input("\nNhập biển số (hoặc 'q' để thoát): ").strip().upper()

            if bien_so == "Q":
                print("👋 Thoát chương trình.")
                break

            if not bien_so:
                print("⚠️  Vui lòng nhập biển số!")
                continue

            tra_cuu_phat_nguoi(driver, bien_so)

            tiep = input("\nTra cứu tiếp? (Enter để tiếp / q để thoát): ").strip().lower()
            if tiep == "q":
                print("👋 Thoát chương trình.")
                break

    finally:
        driver.quit()
        print("✅ Đã đóng trình duyệt.")