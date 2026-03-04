import sys
sys.stdout.reconfigure(encoding='utf-8')
def sum(a,b):
    return a+b
def tongsochan(n):
    tong = 0
    for i in range(1, n+1):
        if i%2 == 0:
            tong +=i
    return tong
n = int(input("Nhập n: "))
def tongsole(n):
    tong = 0
    for i in range(1,n+1):
        if i%2 !=0:
            tong +=i
    return tong
def tongsonguyento(n):
    tong = 0
    for i in range(2, n+1):
        songuyento = True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                songuyento = False
                break
        if songuyento:
            tong +=i
    return tong
#ghi đè
def say_hello():
    print("Xin chào!")
#check biến toàn cục
bien_toan_cuc = 10
print("Biến toàn cục:",bien_toan_cuc)
def ham_bien_toan_cuc():
    bien_cuc_bo = 5
    bien_toan_cuc = 20
    print("Nhận Biến cục bộ",bien_cuc_bo)
    print("Biến toàn cục",bien_toan_cuc)
ham_bien_toan_cuc()
print("Biến toàn cục bên ngoài hàm:", bien_toan_cuc)
tongchan = tongsochan(n)
tongle = tongsole(n)
tongnguyento = tongsonguyento(n)
result = sum(5,10)

print("Tổng các số lẻ từ 1 đến", n, "là:", tongle)
print("Tổng các số chẵn từ 1 đến", n, "là:", tongchan)
print("Tổng các số nguyên tố từ 1 đến", n, "là:", tongnguyento)
print("Tổng của 5 và 10 là:", result)