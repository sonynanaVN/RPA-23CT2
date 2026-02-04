import sys
sys.stdout.reconfigure(encoding='utf-8')
sanpham = 350000
print("Nhập giá tiền bạn đang có:")
tien_hien_co = int(input())
if tien_hien_co == sanpham:
    print("Bạn vừa đủ tiền để mua sản phẩm.")
elif tien_hien_co > sanpham:
    print("Bạn có đủ tiền để mua sản phẩm và còn dư.")
else:
    print("Bạn không đủ tiền để mua sản phẩm.")