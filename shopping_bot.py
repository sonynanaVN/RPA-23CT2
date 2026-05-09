"""
BOT MUA HÀNG TỰ ĐỘNG - automationexercise.com
Trình duyệt: Google Chrome
Yêu cầu: pip install selenium webdriver-manager
"""

import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# ============================================================
# ⚙️ CẤU HÌNH - Thay đổi thông tin tại đây
# ============================================================
CONFIG = {
    # Tài khoản đăng nhập
    "email": "rokhananana98@gmail.com",
    "password": "mwewleecdujetfxw",
    "name": "Nguyen Van A",

    # Thông tin đặt hàng
    "address": "123 Duong ABC, Ha Noi",
    "comment": "Giao hang nhanh giup toi nha!",

    # Thông tin thẻ giả (test)
    "card_name": "Nguyen Van A",
    "card_number": "4111111111111111",
    "card_cvc": "123",
    "card_expiry_month": "12",
    "card_expiry_year": "2027",

    # Email thông báo (Gmail)
    "sender_email": "your_gmail@gmail.com",
    "sender_password": "your_app_password",   # Gmail App Password 16 ký tự
    "receiver_email": "your_email@gmail.com",

    # Từ khóa tìm kiếm
    "search_keyword": "shirt",

    # Hiển thị trình duyệt (False = ẩn)
    "headless": False,
}

BASE_URL = "https://www.automationexercise.com"


# ============================================================
# 🤖 CLASS BOT CHÍNH
# ============================================================
class ShoppingBot:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.order_result = {
            "success": False,
            "product_name": "",
            "product_price": "",
            "message": ""
        }

    # ----------------------------------------------------------
    # Khởi tạo trình duyệt Chrome
    # ----------------------------------------------------------
    def setup_driver(self):
        print("🚀 Khởi động Google Chrome...")
        options = webdriver.ChromeOptions()

        if CONFIG["headless"]:
            options.add_argument("--headless")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--window-size=1366,768")
        options.add_argument("--incognito")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 15)

        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        print("✅ Google Chrome sẵn sàng!")

    # ----------------------------------------------------------
    # Tiện ích
    # ----------------------------------------------------------
    def sleep(self, seconds=1):
        time.sleep(seconds)

    def find(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def click(self, by, value, timeout=10):
        elem = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        self.sleep(0.5)
        elem.click()
        return elem

    def type_text(self, by, value, text, clear=True):
        elem = self.find(by, value)
        if clear:
            elem.clear()
        elem.send_keys(text)
        return elem

    def close_ads(self):
        try:
            close_btn = self.driver.find_element(
                By.CSS_SELECTOR, "div#ad_position_box button.fc-close"
            )
            close_btn.click()
            self.sleep(0.5)
        except Exception:
            pass

    # ----------------------------------------------------------
    # BƯỚC 1: Login
    # ----------------------------------------------------------
    def login(self):
        print("\n📌 BƯỚC 1: Đăng nhập...")
        self.driver.get(f"{BASE_URL}/login")
        self.sleep(2)
        self.close_ads()

        self.type_text(By.CSS_SELECTOR, "input[data-qa='login-email']", CONFIG["email"])
        self.type_text(By.CSS_SELECTOR, "input[data-qa='login-password']", CONFIG["password"])
        self.click(By.CSS_SELECTOR, "button[data-qa='login-button']")
        self.sleep(2)

        try:
            logged_in = self.driver.find_element(
                By.XPATH, "//a[contains(text(), 'Logged in as')]"
            )
            print(f"✅ Đăng nhập thành công: {logged_in.text}")
            return True
        except NoSuchElementException:
            print("❌ Đăng nhập thất bại! Kiểm tra email/password.")
            return False

    # ----------------------------------------------------------
    # BƯỚC 2 & 3: Truy cập Products và tìm kiếm
    # ----------------------------------------------------------
    def search_products(self):
        print(f"\n📌 BƯỚC 2-3: Tìm kiếm '{CONFIG['search_keyword']}'...")
        self.driver.get(f"{BASE_URL}/products")
        self.sleep(2)
        self.close_ads()

        self.type_text(By.ID, "search_product", CONFIG["search_keyword"])
        self.click(By.ID, "submit_search")
        self.sleep(2)
        self.close_ads()

        products = self.driver.find_elements(By.CSS_SELECTOR, ".productinfo")
        print(f"✅ Tìm thấy {len(products)} sản phẩm!")
        return len(products) > 0

    # ----------------------------------------------------------
    # BƯỚC 4 & 5: Lọc và chọn sản phẩm giá thấp nhất
    # ----------------------------------------------------------
    def select_cheapest_product(self):
        print("\n📌 BƯỚC 4-5: Chọn sản phẩm giá thấp nhất...")

        products = self.driver.find_elements(By.CSS_SELECTOR, ".single-products")
        cheapest_price = float("inf")
        cheapest_index = 0
        product_data = []

        for i, product in enumerate(products):
            try:
                price_text = product.find_element(By.CSS_SELECTOR, ".productinfo h2").text
                name_text = product.find_element(By.CSS_SELECTOR, ".productinfo p").text
                price = float(price_text.replace("Rs.", "").replace(",", "").strip())
                product_data.append({
                    "index": i,
                    "name": name_text,
                    "price": price,
                    "price_text": price_text
                })
                if price < cheapest_price:
                    cheapest_price = price
                    cheapest_index = i
                print(f"  [{i}] {name_text} - {price_text}")
            except Exception:
                continue

        if not product_data:
            print("❌ Không lấy được thông tin sản phẩm!")
            return False

        chosen = product_data[cheapest_index]
        self.order_result["product_name"] = chosen["name"]
        self.order_result["product_price"] = chosen["price_text"]
        print(f"\n✅ Chọn rẻ nhất: {chosen['name']} - {chosen['price_text']}")

        # BƯỚC 6: Thêm vào giỏ hàng
        print("\n📌 BƯỚC 6: Thêm vào giỏ hàng...")
        add_btns = self.driver.find_elements(
            By.CSS_SELECTOR, ".productinfo a.add-to-cart"
        )

        if cheapest_index < len(add_btns):
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", add_btns[cheapest_index]
            )
            self.sleep(0.5)
            add_btns[cheapest_index].click()
            self.sleep(2)
        else:
            from selenium.webdriver.common.action_chains import ActionChains
            product_elem = products[cheapest_index]
            ActionChains(self.driver).move_to_element(product_elem).perform()
            self.sleep(0.5)
            btn = product_elem.find_element(By.CSS_SELECTOR, "a.add-to-cart")
            btn.click()
            self.sleep(2)

        # Đóng modal
        try:
            btns = WebDriverWait(self.driver, 3).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, "#cartModal .btn")
                )
            )
            for btn in btns:
                if "continue" in btn.text.lower():
                    btn.click()
                    break
        except Exception:
            pass

        print("✅ Đã thêm vào giỏ hàng!")
        return True

    # ----------------------------------------------------------
    # BƯỚC 7: Vào Cart và verify
    # ----------------------------------------------------------
    def verify_cart(self):
        print("\n📌 BƯỚC 7: Kiểm tra giỏ hàng...")
        self.driver.get(f"{BASE_URL}/view_cart")
        self.sleep(2)
        self.close_ads()

        cart_items = self.driver.find_elements(
            By.CSS_SELECTOR, "#cart_info_table tbody tr"
        )
        print(f"✅ Giỏ hàng có {len(cart_items)} sản phẩm!")

        try:
            qty = self.driver.find_element(
                By.CSS_SELECTOR, ".cart_quantity button"
            ).text
            print(f"✅ Số lượng: {qty}")
        except Exception:
            pass

        return len(cart_items) > 0

    # ----------------------------------------------------------
    # BƯỚC 8: Proceed to Checkout
    # ----------------------------------------------------------
    def proceed_to_checkout(self):
        print("\n📌 BƯỚC 8: Tiến hành thanh toán...")
        self.click(By.CSS_SELECTOR, "a.btn.check_out")
        self.sleep(2)
        self.close_ads()
        print("✅ Đã vào trang checkout!")

    # ----------------------------------------------------------
    # BƯỚC 9: Điền comment
    # ----------------------------------------------------------
    def fill_order_comment(self):
        print("\n📌 BƯỚC 9: Điền comment đơn hàng...")
        try:
            comment_box = self.find(By.NAME, "message")
            comment_box.clear()
            comment_box.send_keys(CONFIG["comment"])
            print("✅ Đã điền comment!")
        except Exception:
            print("⚠️ Không tìm thấy ô comment, bỏ qua.")

    # ----------------------------------------------------------
    # BƯỚC 10: Place Order
    # ----------------------------------------------------------
    def place_order(self):
        print("\n📌 BƯỚC 10: Đặt hàng...")
        self.click(By.CSS_SELECTOR, "a.btn.check_out, a[href='/payment']")
        self.sleep(2)
        print("✅ Đã nhấn Place Order!")

    # ----------------------------------------------------------
    # BƯỚC 11: Điền thông tin thanh toán
    # ----------------------------------------------------------
    def fill_payment(self):
        print("\n📌 BƯỚC 11: Điền thông tin thẻ...")
        self.type_text(By.CSS_SELECTOR, "input[data-qa='name-on-card']", CONFIG["card_name"])
        self.type_text(By.CSS_SELECTOR, "input[data-qa='card-number']", CONFIG["card_number"])
        self.type_text(By.CSS_SELECTOR, "input[data-qa='cvc']", CONFIG["card_cvc"])
        self.type_text(By.CSS_SELECTOR, "input[data-qa='expiry-month']", CONFIG["card_expiry_month"])
        self.type_text(By.CSS_SELECTOR, "input[data-qa='expiry-year']", CONFIG["card_expiry_year"])
        print("✅ Đã điền thông tin thẻ!")

    # ----------------------------------------------------------
    # BƯỚC 12: Xác nhận đặt hàng
    # ----------------------------------------------------------
    def confirm_order(self):
        print("\n📌 BƯỚC 12: Xác nhận đặt hàng...")
        self.click(By.CSS_SELECTOR, "button[data-qa='pay-button']")
        self.sleep(3)

        try:
            success_msg = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "h2[data-qa='order-placed'], .order-placed, #success_message")
                )
            )
            print(f"🎉 ĐẶT HÀNG THÀNH CÔNG! {success_msg.text}")
            self.order_result["success"] = True
            self.order_result["message"] = "Đặt hàng thành công!"
            return True
        except TimeoutException:
            if "order_placed" in self.driver.current_url or "payment_done" in self.driver.current_url:
                print("🎉 ĐẶT HÀNG THÀNH CÔNG!")
                self.order_result["success"] = True
                self.order_result["message"] = "Đặt hàng thành công!"
                return True
            else:
                print("❌ Không xác nhận được đặt hàng thành công.")
                self.order_result["message"] = "Không xác nhận được kết quả."
                return False

    # ----------------------------------------------------------
    # BƯỚC 13: Gửi email thông báo
    # ----------------------------------------------------------
    def send_email(self):
        print("\n📌 BƯỚC 13: Gửi email thông báo...")
        status = "✅ THÀNH CÔNG" if self.order_result["success"] else "❌ THẤT BẠI"

        html_body = f"""
        <html><body>
        <h2>🛒 Kết quả đặt hàng tự động</h2>
        <p><b>Trạng thái:</b> {status}</p>
        <hr>
        <p><b>🏷️ Sản phẩm:</b> {self.order_result['product_name']}</p>
        <p><b>💰 Giá:</b> {self.order_result['product_price']}</p>
        <p><b>📝 Ghi chú:</b> {self.order_result['message']}</p>
        <hr>
        <p><b>🌐 Website:</b> {BASE_URL}</p>
        <p><b>🔍 Từ khóa:</b> {CONFIG['search_keyword']}</p>
        <p><b>🌐 Trình duyệt:</b> Google Chrome</p>
        <p><i>Email được gửi tự động bởi Shopping Bot 🤖</i></p>
        </body></html>
        """

        try:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = f"[Shopping Bot] {status} - {self.order_result['product_name']}"
            msg["From"] = CONFIG["sender_email"]
            msg["To"] = CONFIG["receiver_email"]
            msg.attach(MIMEText(html_body, "html"))

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(CONFIG["sender_email"], CONFIG["sender_password"])
                server.sendmail(
                    CONFIG["sender_email"],
                    CONFIG["receiver_email"],
                    msg.as_string()
                )
            print(f"✅ Đã gửi email tới {CONFIG['receiver_email']}!")
        except Exception as e:
            print(f"⚠️ Không gửi được email: {e}")
            print("💡 Tip: Dùng Gmail App Password tại myaccount.google.com/apppasswords")

    # ----------------------------------------------------------
    # CHẠY TOÀN BỘ FLOW
    # ----------------------------------------------------------
    def run(self):
        print("=" * 60)
        print("🤖 SHOPPING BOT - Google Chrome")
        print("🌐 automationexercise.com")
        print("=" * 60)

        try:
            self.setup_driver()

            if not self.login():
                raise Exception("Đăng nhập thất bại!")

            if not self.search_products():
                raise Exception("Không tìm thấy sản phẩm!")

            if not self.select_cheapest_product():
                raise Exception("Không thể chọn sản phẩm!")

            if not self.verify_cart():
                raise Exception("Giỏ hàng trống!")

            self.proceed_to_checkout()
            self.fill_order_comment()
            self.place_order()
            self.fill_payment()
            self.confirm_order()

        except Exception as e:
            print(f"\n❌ LỖI: {e}")
            self.order_result["message"] = str(e)

        finally:
            self.send_email()

            print("\n" + "=" * 60)
            print("📊 KẾT QUẢ CUỐI CÙNG:")
            print(f"  Trạng thái : {'✅ THÀNH CÔNG' if self.order_result['success'] else '❌ THẤT BẠI'}")
            print(f"  Sản phẩm   : {self.order_result['product_name']}")
            print(f"  Giá        : {self.order_result['product_price']}")
            print(f"  Ghi chú    : {self.order_result['message']}")
            print(f"  Trình duyệt: Google Chrome")
            print("=" * 60)

            if self.driver:
                self.sleep(2)
                self.driver.quit()
                print("👋 Đã đóng Chrome!")


# ============================================================
# 🚀 CHẠY BOT
# ============================================================
if __name__ == "__main__":
    bot = ShoppingBot()
    bot.run()