import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# =========================
# 1. CREATE - POST
# =========================
print("===== CREATE POST =====")

new_post = {
    "title": "Bài viết mới",
    "body": "Nội dung demo bằng Python",
    "userId": 1
}

response = requests.post(f"{BASE_URL}/posts", json=new_post)

print("Status Code:", response.status_code)
print("Response:")
print(response.json())

print("\n")


# =========================
# 2. GET ALL POSTS
# =========================
print("===== GET ALL POSTS =====")

response = requests.get(f"{BASE_URL}/posts")

print("Status Code:", response.status_code)

posts = response.json()

# In thử 3 bài đầu
for post in posts[:3]:
    print(post)

print("\n")


# =========================
# 3. GET SINGLE POST
# =========================
print("===== GET SINGLE POST =====")

response = requests.get(f"{BASE_URL}/posts/1")

print("Status Code:", response.status_code)
print(response.json())

print("\n")


# =========================
# 4. UPDATE POST - PUT
# =========================
print("===== UPDATE POST =====")

updated_post = {
    "id": 1,
    "title": "Tiêu đề đã cập nhật",
    "body": "Nội dung đã cập nhật",
    "userId": 1
}

response = requests.put(
    f"{BASE_URL}/posts/1",
    json=updated_post
)

print("Status Code:", response.status_code)
print(response.json())

print("\n")


# =========================
# 5. DELETE POST
# =========================
print("===== DELETE POST =====")

response = requests.delete(f"{BASE_URL}/posts/1")

print("Status Code:", response.status_code)
print("Response:", response.text)

print("\n")
print("🎉 Hoàn thành CRUD API!")