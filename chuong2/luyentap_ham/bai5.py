def la_so_hoan_hao(n):
    if n <= 1:
        return False
    tong = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            tong += i
            if i != n // i:
                tong += n // i
        i += 1
    return tong == n
a = int(input("Nhập số n: "))
if la_so_hoan_hao(a):
    print(f"{a} là số hoàn hảo")
else:
    print(f"{a} không phải số hoàn hảo")
