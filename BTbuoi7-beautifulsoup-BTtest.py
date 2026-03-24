from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <h1>Tiêu đề chính</h1>
    <p>Bài viết số 1</p>
    <p>Bài viết số 2</p>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Lấy tiêu đề
title = soup.h1.text
print("Tiêu đề:", title)

# Lấy tất cả thẻ <p>
paragraphs = soup.find_all("p")

for p in paragraphs:
    print("Nội dung:", p.text)