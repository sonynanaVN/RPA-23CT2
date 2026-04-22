from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

URL = "https://www.google.com"
driver.get(URL)

time.sleep(2)
print(driver.title)

driver.quit()