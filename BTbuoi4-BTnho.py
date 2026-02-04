#câu 1
tentui=str(input("Nhập tên của bạn: "))
tuoi=int(input("Nhập tuổi của bạn: "))
diemtb=float(input("Nhập điểm trung bình của bạn: "))
print(f"Chào bạn {tentui}, bạn {tuoi} tuổi và có điểm trung bình là {diemtb}.")
#câu 2
cd=float(input("Nhập chiều dài hình chữ nhật: "))
cr=float(input("Nhập chiều rộng hình chữ nhật: "))
dt=cd*cr
cv=(cd+cr)*2
print(f"Diện tích hình chữ nhật là: {dt}")
print(f"Chu vi hình chữ nhật là: {cv}")
#câu 3:Chuyển nhiệt độ từ độ C sang độ F
c=float(input("Nhập nhiệt độ độ C: "))
f=(9/5)*c+32
print(f"Nhiệt độ độ F là: {f}")
#câu 4:Kiểm tra chẵn lẻ
num=int(input("Nhập một số nguyên: "))
if num % 2 == 0:
    print(f"Số {num} là số chẵn.")
else:
    print(f"Số {num} là số lẻ.")
#câu 5:tổng hiệu thương 2 số thực
num1=float(input("Nhập số thực thứ nhất: "))
num2=float(input("Nhập số thực thứ hai: "))
tong=num1+num2
hieu=num1-num2  
thuong=num1/num2
print(f"Tổng:{tong},Hiệu:{hieu},Thương:{thuong}")