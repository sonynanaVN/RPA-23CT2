from bs4 import BeautifulSoup
import requests
import pandas as pd
URL = "https://books.toscrape.com/"
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

book_product = soup.find_all("article", class_="product_pod")
data = []
for book in book_product:
    name = book.h3.a["title"]
    print(f"Tên sách: {name}")
    price = book.find("p", class_="price_color").text
    print(f"Giá: {price}")
    in_stock = book.find("p", class_="instock availability").text.strip()
    print(f"Tình trạng: {in_stock}")
    startting = book.find("p", class_="star-rating")["class"][1]
    print(f"Đánh giá: {startting} starts")
    print("-" * 30)
data.append({
    "Tên sách": name,
    "Giá": price,
    "Tình trạng": in_stock,
    "Đánh giá": startting
})
df = pd.DataFrame(data)
df.to_excel("Pandas.xlsx", index=False,engine="openpyxl")
print("Dữ liệu đã được lưu vào Pandas.xlsx")
#homework : Lấy dữ liệu từ 10 trang đầu tiên của website và lưu vào Excel, sau đó thống kê số lượng sách theo từng đánh giá (1-5 sao) và giá trung bình của mỗi loại đánh giá.