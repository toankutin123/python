n = int(input("Nhap so nguyen n: "))
dem = 1
tich = 1
while dem <= n:
    tich = tich * dem
    dem = dem + 1
print("Giai thua cua", n, "la:", tich)