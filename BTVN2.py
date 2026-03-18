import sys
sys.stdout.reconfigure(encoding='utf-8')
# Khai báo dữ liệu
von = 100_000_000     
lai_suat = 0.05        
so_nam = 3

# Tính tiền lãi (lãi đơn)
lai = von * lai_suat * so_nam

# Tính tổng tiền nhận được
tong_tien = von + lai

# Tính lãi trung bình mỗi tháng
so_thang = so_nam * 12
lai_trung_binh_thang = lai / so_thang

# In kết quả
print("Tiền lãi sau 3 năm:", lai, "VND")
print("Tổng tiền nhận được:", tong_tien, "VND")
print("Lãi trung bình mỗi tháng:", round(lai_trung_binh_thang), "VND")