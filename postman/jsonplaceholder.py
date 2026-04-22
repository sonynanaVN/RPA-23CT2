import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

print("===== CREATE POST =====")

new_post = {
    "title": "Bài viết mới",
    "body": "Nội dung demo bằng Python",
    "userId": 1
}

response = requests.post(f"{BASE_URL}/posts", json=new_post)

print("Status Code:", response.status_code)
print(response.json())

print("\n")


print("===== GET ALL POSTS =====")

response = requests.get(f"{BASE_URL}/posts")

print("Status Code:", response.status_code)

posts = response.json()

for post in posts:
    print("ID:", post["id"])

print("\n")


print("===== GET SINGLE POST =====")

response = requests.get(f"{BASE_URL}/posts/1")

print("Status Code:", response.status_code)

post = response.json()

print("ID:", post["id"])
print("Title:", post["title"])
print("Body:", post["body"])
print("User ID:", post["userId"])

print("\n")


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


print("===== DELETE POST =====")

response = requests.delete(f"{BASE_URL}/posts/1")

print("Status Code:", response.status_code)
print("Response:", response.text)

print("\n")
print(" Hoàn thành CRUD API!")