import cloudscraper
from bs4 import BeautifulSoup

def tra_cuu_phat_nguoi(bien_so):
    scraper = cloudscraper.create_scraper()
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://phatnguoi.com/",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    
    # Gửi POST request với biển số
    data = {"BienKiemSoat": bien_so}
    
    response = scraper.post(
        "https://phatnguoi.com/",
        headers=headers,
        data=data,
        timeout=15
    )
    
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Tìm kết quả trong HTML (tuỳ cấu trúc site)
        result = soup.find("div", class_="result")  # cần inspect site để biết class thật
        
        if result:
            print("\n===== KẾT QUẢ =====")
            print(result.get_text(strip=True))
        else:
            # In toàn bộ text để debug
            print("\n===== NỘI DUNG TRANG =====")
            print(soup.get_text(separator="\n", strip=True)[:2000])
    else:
        print(f"Lỗi: {response.status_code}")

# ===== CHẠY CHƯƠNG TRÌNH =====
if __name__ == "__main__":
    print("=" * 40)
    print("   TRA CỨU PHẠT NGUỘI BIỂN SỐ XE")
    print("=" * 40)
    
    while True:
        bien_so = input("\nNhập biển số xe (hoặc 'q' để thoát): ").strip().upper()
        
        if bien_so == "Q":
            print("Thoát chương trình.")
            break
        
        if not bien_so:
            print("Vui lòng nhập biển số!")
            continue
        
        print(f"\nĐang tra cứu: {bien_so} ...")
        tra_cuu_phat_nguoi(bien_so)
        print("-" * 40)
