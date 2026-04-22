import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import pandas as pd
import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8')

data = {
    "MaSV": ["SV01","SV02","SV03","SV04","SV05","SV06","SV07","SV08","SV09","SV10"],
    "HoTen": ["An","Binh","Cuong","Dung","Huy","Khanh","Linh","Minh","Nam","Phuc"],
    "Lop": ["CT1","CT1","CT2","CT2","CT1","CT3","CT3","CT2","CT1","CT3"],
    "DiemPython": [8, 7, None, 9, 6, 7.5, None, 8.5, 5, 6],
    "DiemWeb": [7, None, 8, 9, 6, 7, 8, None, 5, 6],
    "DiemDatabase": [8, 7, 9, None, 6, 7, 8, 9, None, 6]
}

df = pd.DataFrame(data)

print("=== Data ban đầu ===")
print(df)

# 2. Kiểm tra dữ liệu null
print("\n=== Kiểm tra null ===")
print(df.isnull().sum())

# 3. Điền null bằng 0
df = df.fillna(0)

# 4. Tạo cột Điểm trung bình
df["DiemTB"] = (df["DiemPython"] + df["DiemWeb"] + df["DiemDatabase"]) / 3

# 5. Xếp loại
def xep_loai(diem):
    if diem >= 8:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["XepLoai"] = df["DiemTB"].apply(xep_loai)

print("\n=== Sau khi xử lý ===")
print(df)

# 6. Thống kê theo lớp
print("\n=== Thống kê theo lớp ===")
print(df.groupby("Lop").count())

# 7. Điểm trung bình mỗi lớp
print("\n=== Điểm TB mỗi lớp ===")
print(df.groupby("Lop")["DiemTB"].mean())

# 8. Tạo bảng Thông tin lớp
lop_data = {
    "Lop": ["CT1","CT2","CT3"],
    "GiaoVien": ["Thầy A","Thầy B","Thầy C"],
    "PhongHoc": ["P101","P102","P103"]
}

df_lop = pd.DataFrame(lop_data)

# 9. Ghép bảng
df_merge = pd.merge(df, df_lop, on="Lop")

print("\n=== Bảng sau khi ghép ===")
print(df_merge)