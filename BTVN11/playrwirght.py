from playwright.sync_api import sync_playwright
import smtplib
from email.mime.text import MIMEText

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

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.automationexercise.com")

    page.click("text=Signup / Login")

    page.fill("input[data-qa='login-email']", "ngovan15121977@gmail.com")
    page.fill("input[data-qa='login-password']", "0702749422Ads!")
    page.click("button[data-qa='login-button']")

    page.wait_for_timeout(3000)

    page.click("a[href='/products']")

    page.fill("#search_product", "shirt")
    page.click("#submit_search")

    page.wait_for_timeout(2000)

    products = page.locator(".product-image-wrapper")

    min_price = 10**9
    best_index = 0

    for i in range(products.count()):
        text = products.nth(i).inner_text()

        if "Rs." not in text:
            continue

        try:
            price = int(text.split("Rs.")[1].split()[0])

            if price < min_price:
                min_price = price
                best_index = i
        except:
            continue

    products.nth(best_index).locator("text=Add to cart").click()

    page.wait_for_timeout(2000)

    page.click("text=View Cart")

    qty = page.locator(".disabled").inner_text()
    assert qty == "1"

    page.click("text=Proceed To Checkout")

    page.click("text=Place Order")

    page.fill("input[name='name_on_card']", "Test User")
    page.fill("input[name='card_number']", "4111111111111111")
    page.fill("input[name='cvc']", "123")
    page.fill("input[name='expiry_month']", "12")
    page.fill("input[name='expiry_year']", "2030")

    page.click("#submit")

    result = page.locator("h2").inner_text()
    print("ORDER RESULT:", result)

    browser.close()

    send_email(result)