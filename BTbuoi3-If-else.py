#nhập điểm tb
diem=float(input("Nhập điểm trung bình của bạn: "))
if diem >= 8.5:
    print("Bạn đạt loại Giỏi.")
elif diem >= 7.0:
    print("Bạn đạt loại Khá.")
elif diem >= 5.0:
    print("Bạn đạt loại Trung bình.")
else:
    print("Bạn đạt loại Yếu.")