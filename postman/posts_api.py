import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"

def print_response(label, response):
    print(f"\n{'='*50}")
    print(f" {label}")
    print(f" {response.request.method} {response.url}")
    print(f" Status Code: {response.status_code}")
    print(f" Response:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    print(f"{'='*50}")


# ──────────────────────────────────────────
# 1. CREATE – POST /posts
# ──────────────────────────────────────────
def create_post():
    payload = {
        "title": "Bài viết mới",
        "body": "Đây là nội dung bài viết được tạo bằng POST request.",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    print_response("TẠO BÀI VIẾT (POST /posts)", response)


# ──────────────────────────────────────────
# 2. GET ALL – GET /posts
# ──────────────────────────────────────────
def get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    # Chỉ in 3 bài đầu để dễ đọc
    data = response.json()[:20]
    print(f"\n{'='*50}")
    print(f" LẤY DANH SÁCH BÀI VIẾT (GET /posts)")
    print(f" GET {BASE_URL}/posts")
    print(f" Status Code: {response.status_code}")
    print(f" Tổng số bài viết: {len(response.json())}")
    print(f" 20 bài đầu tiên:")
    print(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"{'='*50}")


# ──────────────────────────────────────────
# 3. GET ONE – GET /posts/1
# ──────────────────────────────────────────
def get_post_by_id(post_id=1):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    print_response(f"LẤY CHI TIẾT BÀI VIẾT (GET /posts/{post_id})", response)


# ──────────────────────────────────────────
# 4. UPDATE – PUT /posts/1
# ──────────────────────────────────────────
def update_post(post_id=1):
    payload = {
        "id": post_id,
        "title": "Tiêu đề đã được cập nhật",
        "body": "Nội dung mới sau khi cập nhật bằng PUT request.",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=payload)
    print_response(f"CẬP NHẬT BÀI VIẾT (PUT /posts/{post_id})", response)


# ──────────────────────────────────────────
# 5. DELETE – DELETE /posts/1
# ──────────────────────────────────────────
def delete_post(post_id=1):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    print(f"\n{'='*50}")
    print(f"📌 XÓA BÀI VIẾT (DELETE /posts/{post_id})")
    print(f"🔗 DELETE {BASE_URL}/posts/{post_id}")
    print(f"✅ Status Code: {response.status_code}")
    print(f"📦 Response: {response.json()}")
    print(f"{'='*50}")


# ──────────────────────────────────────────
# RUN ALL
# ──────────────────────────────────────────
if __name__ == "__main__":
    create_post()
    get_all_posts()
    get_post_by_id(1)
    update_post(1)
    delete_post(1)