import sys
sys.stdout.reconfigure(encoding='utf-8')
# Số tiền ban đầu
so_tien_ban_dau = 2_000_000

# Chi phí
mua_ao_quan = 1_000_000
mua_do_an = 1_550_000
di_lam_them = 3_000_000  # Đây là thu nhập

# Tính toán
tong_chi = mua_ao_quan + mua_do_an
tong_thu = di_lam_them
so_tien_con_lai = so_tien_ban_dau - tong_chi + tong_thu

# In kết quả
print("=== TÍNH TOÁN CHI TIẾT ===")
print(f"Số tiền ban đầu: {so_tien_ban_dau:,} đồng")
print(f"\nChi phí:")
print(f"  - Mua áo quần: {mua_ao_quan:,} đồng")
print(f"  - Mua đồ ăn: {mua_do_an:,} đồng")
print(f"  - Tổng chi: {tong_chi:,} đồng")
print(f"\nThu nhập:")
print(f"  - Đi làm thêm: {tong_thu:,} đồng")
print(f"\nSố tiền còn lại: {so_tien_con_lai:,} đồng")