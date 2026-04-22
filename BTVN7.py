import pandas as pd
import numpy as np
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

data_sv = {
    'MaSV':        ['SV001','SV002','SV003','SV004','SV005',
                    'SV006','SV007','SV008','SV009','SV010'],
    'HoTen':       ['Nguyen Van An','Tran Thi Bich','Le Van Cuong','Pham Thi Dung','Hoang Van Em',
                    'Nguyen Thi Fong','Bui Van Giang','Do Thi Hoa','Vu Van Hung','Dang Thi Yen'],
    'Lop':         ['CNTT1','CNTT1','CNTT2','CNTT2','CNTT3',
                    'CNTT3','CNTT1','CNTT2','CNTT3','CNTT1'],
    'DiemPython':  [8.5, 7.0, None, 6.0, 9.0, 5.5, None, 4.0, 7.5, 8.0],
    'DiemWeb':     [7.0, None, 8.0, 5.5, 8.5, 6.0, 7.0, None, 6.5, 9.0],
    'DiemDatabase':[9.0, 6.5, 7.5, None, 7.0, 5.0, 6.0, 4.5, None, 8.5]
}

df_sv = pd.DataFrame(data_sv)
print("=" * 55)
print("1. BẢNG DỮ LIỆU SINH VIÊN")
print("=" * 55)
print(df_sv.to_string(index=False))


df_sv.to_csv('sinh_vien.csv', index=False)
df_sv = pd.read_csv('sinh_vien.csv')

print("\n" + "=" * 55)
print("2. KIỂM TRA DỮ LIỆU NULL")
print("=" * 55)
print("\nSố lượng null theo từng cột:")
print(df_sv.isnull().sum())
print(f"\nTổng số ô null: {df_sv.isnull().sum().sum()}")

df_sv[['DiemPython','DiemWeb','DiemDatabase']] = \
    df_sv[['DiemPython','DiemWeb','DiemDatabase']].fillna(0)

print("\n" + "=" * 55)
print("3. SAU KHI ĐIỀN NULL = 0")
print("=" * 55)
print(df_sv.to_string(index=False))
print(f"\nTổng số ô null còn lại: {df_sv.isnull().sum().sum()}")


df_sv['DiemTB'] = ((df_sv['DiemPython'] + df_sv['DiemWeb'] + df_sv['DiemDatabase']) / 3).round(2)

print("\n" + "=" * 55)
print("4. CỘT ĐIỂM TRUNG BÌNH")
print("=" * 55)
print(df_sv[['MaSV','HoTen','DiemPython','DiemWeb','DiemDatabase','DiemTB']].to_string(index=False))


def xep_loai(diem):
    if diem >= 8:
        return 'Gioi'
    elif diem >= 6.5:
        return 'Kha'
    elif diem >= 5:
        return 'Trung Binh'
    else:
        return 'Yeu'

df_sv['XepLoai'] = df_sv['DiemTB'].apply(xep_loai)

print("\n" + "=" * 55)
print("5. CỘT XẾP LOẠI")
print("=" * 55)
print(df_sv[['MaSV','HoTen','DiemTB','XepLoai']].to_string(index=False))

print("\n" + "=" * 55)
print("6. THỐNG KÊ THEO LỚP")
print("=" * 55)
thong_ke = df_sv.groupby('Lop').agg(
    So_Sinh_Vien   = ('MaSV',    'count'),
    SL_Gioi        = ('XepLoai', lambda x: (x == 'Gioi').sum()),
    SL_Kha         = ('XepLoai', lambda x: (x == 'Kha').sum()),
    SL_Trung_Binh  = ('XepLoai', lambda x: (x == 'Trung Binh').sum()),
    SL_Yeu         = ('XepLoai', lambda x: (x == 'Yeu').sum())
).reset_index()
print(thong_ke.to_string(index=False))

print("\n" + "=" * 55)
print("7. ĐIỂM TRUNG BÌNH MỖI LỚP")
print("=" * 55)
dtb_lop = df_sv.groupby('Lop')['DiemTB'].mean().round(2).reset_index()
dtb_lop.columns = ['Lop', 'DiemTB_Lop']
print(dtb_lop.to_string(index=False))


data_lop = {
    'Lop':      ['CNTT1',      'CNTT2',      'CNTT3'],
    'GiaoVien': ['Nguyen Van A','Tran Thi B', 'Le Van C'],
    'PhongHoc': ['P101',        'P202',       'P303']
}
df_lop = pd.DataFrame(data_lop)

print("\n" + "=" * 55)
print("8. BẢNG THÔNG TIN LỚP")
print("=" * 55)
print(df_lop.to_string(index=False))

df_merged = pd.merge(df_sv, df_lop, on='Lop', how='left')

print("\n" + "=" * 55)
print("9. BẢNG GHÉP SINH VIÊN + THÔNG TIN LỚP")
print("=" * 55)
print(df_merged.to_string(index=False))