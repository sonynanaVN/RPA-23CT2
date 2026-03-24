import pandas as pd

data_dict = {
    "Ten": ["An", "Binh", "Cuong"],
    "Lop": ["23CT2", "23CT2", "23CT2"],
    "Diem TB": [8.5, 7.0, 9.0],
    "Tuoi": [20, 21, 19],
    "Dia chi": ["Hanoi", "HCM", "Danang"],
    "Hoc luc": ["Gioi", "Kha", "Gioi"],
    "Tinh trang": ["Tot", "Tot", "Tot"]
}
df = pd.DataFrame(data_dict)
print(df)
#thêm dữ liệu
df.loc[len(df)] = ["Dung", "23CT2", 6.5, 22, "Hue", "Trung binh", "On dinh"]
df.loc[len(df)] = ["Tuan", "23CT2", None, 22, "Hue", "Trung binh", "On dinh"]
#truy xuất cột điểm
print(df["Diem TB"])
print("________________________________________________________________")
print(df.loc[0])
print()
#lấy tên sinh viên ở hàng thứ 2
print(df.loc[1,"Ten"])
print()