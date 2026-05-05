
import pandas as pd

danh_sach_bien_so = [
    "43G1-539.05",
    "36C-357.25",
    "36A-369.34",
    "36D-018.62",
    "36A-942.32",
    "36A-606.96",
    "51A-607.19",
    "30A-967.62",
    "30A-202.51",
    "30H-365.18",
    "29H-448.28",
    "36H-008.18",
]

df = pd.DataFrame(danh_sach_bien_so, columns=["Biển số"])
df.to_excel("bien_so.xlsx", index=False)
print("✅ Đã tạo file bien_so.xlsx thành công!")
print("Nội dung:")
print(df.to_string(index=False))