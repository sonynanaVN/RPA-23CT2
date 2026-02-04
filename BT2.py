import sys
sys.stdout.reconfigure(encoding='utf-8')

# Dữ liệu ban đầu
von = 100_000_000      # VND
lai_suat = 0.05        # 5%/năm
thoi_gian_gui = 5      # năm

# 1. Lãi sau 3 năm (lãi đơn)
lai_3_nam = von * lai_suat * 3

# 2. Tổng tiền sau 5 năm
lai_5_nam = von * lai_suat * thoi_gian_gui
tong_tien = von + lai_5_nam

# 3. Lãi trung bình mỗi tháng (trong 5 năm)
so_thang = thoi_gian_gui * 12
lai_tb_thang = lai_5_nam / so_thang

# In kết quả
print("Lãi sau 3 năm:", f"{lai_3_nam:,.0f}", "VND")
print("Tổng tiền sau 5 năm:", f"{tong_tien:,.0f}", "VND")
print("Lãi trung bình mỗi tháng:", f"{lai_tb_thang:,.0f}", "VND")
