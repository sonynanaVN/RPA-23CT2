from bs4 import BeautifulSoup
import requests

URL = "https://books.toscrape.com/"
response = requests.get(URL)
text_response = response.content.decode("utf-8")
print(text_response)
soup = BeautifulSoup(text_response, "html.parser")

book_product = soup.find_all("article", class_="product_pod")
for i_book in book_product:
    print(i_book)
    name = i_book.h3.a["title"]
print(name)