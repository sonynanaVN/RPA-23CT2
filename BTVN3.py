import sys
sys.stdout.reconfigure(encoding='utf-8')

# -------- Câu 1 --------
# Nhập họ tên, tuổi, điểm trung bình và in ra

print("=== Câu 1 ===")
ho_ten = input("Nhập họ tên: ")
tuoi = int(input("Nhập tuổi: "))
diem_tb = float(input("Nhập điểm trung bình: "))

print("Họ tên:", ho_ten)
print("Tuổi:", tuoi)
print("Điểm trung bình:", diem_tb)


# -------- Câu 2 --------
# Tính diện tích và chu vi hình chữ nhật

print("\n=== Câu 2 ===")
chieu_dai = float(input("Nhập chiều dài: "))
chieu_rong = float(input("Nhập chiều rộng: "))

dien_tich = chieu_dai * chieu_rong
chu_vi = (chieu_dai + chieu_rong) * 2

print("Diện tích:", dien_tich)
print("Chu vi:", chu_vi)


# -------- Câu 3 --------
# Chuyển đổi nhiệt độ từ C sang F

print("\n=== Câu 3 ===")
do_C = float(input("Nhập nhiệt độ (C): "))

do_F = (do_C * 9/5) + 32

print("Nhiệt độ (F):", do_F)


# -------- Câu 4 --------
# Kiểm tra số chẵn hay lẻ

print("\n=== Câu 4 ===")
so = int(input("Nhập số nguyên: "))

if so % 2 == 0:
    print("Đây là số chẵn")
else:
    print("Đây là số lẻ")


# -------- Câu 5 --------
# Tính tổng, hiệu, tích, thương của hai số thực

print("\n=== Câu 5 ===")
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

tong = a + b
hieu = a - b
tich = a * b

print("Tổng:", tong)
print("Hiệu:", hieu)
print("Tích:", tich)

if b != 0:
    thuong = a / b
    print("Thương:", thuong)
else:
    print("Không thể chia cho 0")