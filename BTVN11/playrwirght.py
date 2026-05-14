#Anh-2351220080
from playwright.sync_api import sync_playwright
import smtplib
from email.mime.text import MIMEText
import os

EMAIL = "rokhananana98@gmail.com"
PASSWORD = "zdvctubzkhivpetz"
TO_EMAIL = "rokhananana98@gmail.com"

def send_email(result_text):
    msg = MIMEText(result_text)
    msg["Subject"] = "AutomationExercise Playwright Result"
    msg["From"] = EMAIL
    msg["To"] = TO_EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    os.path.expandvars(r"%PROGRAMFILES%\Google\Chrome\Application\chrome.exe"),
]

chrome_path = None
for path in CHROME_PATHS:
    if os.path.exists(path):
        chrome_path = path
        break

if not chrome_path:
    raise FileNotFoundError("Không tìm thấy Chrome! Hãy cài Chrome hoặc tự điền đường dẫn vào biến chrome_path.")

print(f"Dùng Chrome tại: {chrome_path}")

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        executable_path=chrome_path
    )
    page = browser.new_page()

    page.goto("https://www.automationexercise.com")
    page.wait_for_load_state("networkidle")

    page.click("text=Signup / Login")
    page.wait_for_load_state("networkidle")

    page.fill("input[data-qa='login-email']", "ngovan15121977@gmail.com")
    page.fill("input[data-qa='login-password']", "0702749422Ads!")
    page.click("button[data-qa='login-button']")
    page.wait_for_load_state("networkidle")

    page.click("a[href='/products']")
    page.wait_for_load_state("networkidle")

    page.fill("#search_product", "shirt")
    page.click("#submit_search")
    page.wait_for_load_state("networkidle")

    products = page.locator(".product-image-wrapper")
    count = products.count()

    min_price = 10**9
    best_index = 0

    for i in range(count):
        text = products.nth(i).inner_text()
        if "Rs." not in text:
            continue
        try:
            price = int(text.split("Rs.")[1].strip().split()[0])
            if price < min_price:
                min_price = price
                best_index = i
        except:
            continue

    print(f"Sản phẩm rẻ nhất: index={best_index}, giá=Rs.{min_price}")

    best_product = products.nth(best_index)
    best_product.hover()
    page.wait_for_timeout(500)
    best_product.locator(".add-to-cart").first.click()
    page.wait_for_timeout(2000)
    continue_btn = page.locator("button.close-modal, button:has-text('Continue Shopping')")
    if continue_btn.count() > 0:
        continue_btn.first.click()
        page.wait_for_timeout(500)

    page.click("a[href='/view_cart']")
    page.wait_for_load_state("networkidle")

    qty = page.locator("td.cart_quantity button").first.inner_text()
    print(f"Số lượng trong giỏ: {qty}")
    assert qty.strip() == "1", f"Số lượng không phải 1, thực tế là: {qty}"

    page.click("a:has-text('Proceed To Checkout')")
    page.wait_for_load_state("networkidle")

    page.click("a:has-text('Place Order')")
    page.wait_for_load_state("networkidle")

    page.fill("input[name='name_on_card']", "Test User")
    page.fill("input[name='card_number']", "4111111111111111")
    page.fill("input[name='cvc']", "123")
    page.fill("input[name='expiry_month']", "12")
    page.fill("input[name='expiry_year']", "2030")

    page.click("#submit")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)

    result = page.locator("h2[data-qa='order-placed']").inner_text()
    print("ORDER RESULT:", result)

    browser.close()

    send_email(f"ORDER RESULT: {result}\nSản phẩm rẻ nhất: Rs.{min_price}")