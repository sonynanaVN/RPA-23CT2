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
