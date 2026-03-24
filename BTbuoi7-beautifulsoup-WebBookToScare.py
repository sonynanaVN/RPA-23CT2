import sys
sys.stdout.reconfigure(encoding='utf-8')

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

books = []

# 🔹 Crawl 5 trang
for page in range(1, 6):
    url = base_url.format(page)
    
    response = requests.get(url)
    response.encoding = "utf-8" 
    
    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.find_all("article", class_="product_pod")

    for item in items:
        # 📌 Tên sách
        name = item.h3.a["title"]

        # 📌 Giá (fix lỗi £)
        price_text = item.find("p", class_="price_color").text
        price = float(re.sub(r"[^\d.]", "", price_text))  # 🔥 chắc chắn không lỗi

        # 📌 Rating
        rating_class = item.find("p", class_="star-rating")["class"]
        rating = rating_class[1]

        # 📌 Tình trạng
        stock = item.find("p", class_="instock availability").text.strip()

        books.append({
            "Tên sách": name,
            "Giá": price,
            "Đánh giá": rating,
            "Tình trạng": stock
        })

# 🔹 Tạo DataFrame
df = pd.DataFrame(books)

# ======================
# 📊 Thống kê
# ======================

total_books = len(df)
avg_price = round(df["Giá"].mean(), 2)
rating_count = df["Đánh giá"].value_counts()

max_price_book = df.loc[df["Giá"].idxmax()]
min_price_book = df.loc[df["Giá"].idxmin()]

# 📌 Bảng thống kê chính
stats = [
    ["Tổng số sách", total_books],
    ["Giá trung bình", avg_price],
    ["Sách đắt nhất", max_price_book["Tên sách"]],
    ["Sách rẻ nhất", min_price_book["Tên sách"]],
]

df_stats = pd.DataFrame(stats, columns=["Chỉ số", "Giá trị"])

# 📌 Bảng thống kê rating
df_rating = rating_count.reset_index()
df_rating.columns = ["Đánh giá", "Số lượng"]

# ======================
# 📁 Xuất Excel
# ======================

with pd.ExcelWriter("books_data.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Danh sách Sách", index=False)
    df_stats.to_excel(writer, sheet_name="Thống kê", index=False)
    df_rating.to_excel(writer, sheet_name="Rating", index=False)

print("✅ Done! Đã xuất file books_data.xlsx")