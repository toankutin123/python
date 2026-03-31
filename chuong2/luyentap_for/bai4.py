n = int(input("Nhap so nguyen n: "))
if n < 20:
    for i in range(n, 21):
        if i % 5 == 0 or i % 7 == 0:
            print(i)
else:
    print("Nhap n nho hon 20")
