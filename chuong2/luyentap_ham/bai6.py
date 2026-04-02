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


def so_hoan_hao_trong_khoang(a, b):
    result = []
    for x in range(max(2, a), b + 1):
        if la_so_hoan_hao(x):
            result.append(x)
    return result


a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
if a > b:
    a, b = b, a

ket_qua = so_hoan_hao_trong_khoang(a, b)
if ket_qua:
    print(f"Các số hoàn hảo trong khoảng [{a}, {b}] là: {ket_qua}")
else:
    print(f"Không có số hoàn hảo trong khoảng [{a}, {b}].")
