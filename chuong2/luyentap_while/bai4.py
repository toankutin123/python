n = int(input("Nhập số nguyên n: "))
total = 0

for i in range(2, n, 2):
    total += i

print(f"Tổng các số chẵn nhỏ hơn {n}: {total}")