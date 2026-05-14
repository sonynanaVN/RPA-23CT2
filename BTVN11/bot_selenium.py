#Anh-2351220080
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import smtplib
from email.mime.text import MIMEText

EMAIL = "rokhananana98@gmail.com"
PASSWORD = "zdvctubzkhivpetz"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.automationexercise.com")

driver.find_element(By.LINK_TEXT, "Signup / Login").click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='login-email']")))

driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']").send_keys("ngovan15121977@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']").send_keys("0702749422Ads!")
driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()

time.sleep(3)

wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/products']"))).click()

search = wait.until(EC.presence_of_element_located((By.ID, "search_product")))
search.send_keys("shirt")

driver.find_element(By.ID, "submit_search").click()

time.sleep(2)

products = driver.find_elements(By.CLASS_NAME, "product-image-wrapper")

min_price = 10**9
selected = None

for p in products:
    text = p.text

    if "Rs." not in text:
        continue

    try:
        price = int(text.split("Rs.")[1].split()[0])

        if price < min_price:
            min_price = price
            selected = p
    except:
        continue

if selected is None:
    raise Exception(" Không tìm thấy sản phẩm phù hợp")

selected.find_element(By.XPATH, ".//a[contains(text(),'Add to cart')]").click()

time.sleep(2)
driver.find_element(By.LINK_TEXT, "View Cart").click()

qty = driver.find_element(By.CLASS_NAME, "disabled").text
assert qty == "1"

driver.find_element(By.CLASS_NAME, "check_out").click()

driver.find_element(By.LINK_TEXT, "Place Order").click()

wait.until(EC.presence_of_element_located((By.NAME, "name_on_card")))

driver.find_element(By.NAME, "name_on_card").send_keys("Test User")
driver.find_element(By.NAME, "card_number").send_keys("4111111111111111")
driver.find_element(By.NAME, "cvc").send_keys("123")
driver.find_element(By.NAME, "expiry_month").send_keys("12")
driver.find_element(By.NAME, "expiry_year").send_keys("2030")

driver.find_element(By.ID, "submit").click()

result = driver.find_element(By.TAG_NAME, "h2").text
print("Order result:", result)

driver.quit()

def send_email(result_text):
    msg = MIMEText(result_text)
    msg["Subject"] = "Automation Exercise Bot Result"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

send_email(result)