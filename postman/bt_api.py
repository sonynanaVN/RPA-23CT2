import requests
import json
def print_response(label, response):
    print(f"\n{'='*50}")
    print(f" {label}")
    print(f" {response.request.method} {response.url}")
    print(f" Status Code: {response.status_code}")
    print(f" Response:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    print(f"{'='*50}")
BASE_URL = "https://jsonplaceholder.typicode.com"
def create_post():
    payload = {
        "title": "Bài viết mới",
        "body": "Đây là nội dung bài viết được tạo bằng POST request.",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    print_response("TẠO BÀI VIẾT (POST /posts)", response)