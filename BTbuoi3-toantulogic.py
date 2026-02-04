#and or not
print("Nhập điểm TB môn của bạn")
diem = float(input())
print("Bạn có bị kỷ luật không? (nhập 'có' hoặc 'không')")
ky_luat = input().strip().lower()
bi_ky_luat = (ky_luat == 'có')
diemdaccach = float(input("Nhập điểm đặc cách (nếu có, nếu không có nhập 0): "))

if diem >= 8.0 and not bi_ky_luat or diemdaccach == 9.0:
    print("Bạn được học bổng.")
else:
    print("Bạn không được học bổng.")