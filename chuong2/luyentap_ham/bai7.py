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


def tim_so_nguyen_to(a, b):
    primes = []
    start = max(2, a)
    for i in range(start, b + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


def tinh_tong(a, b):
    return a + b


def so_hoan_hao_trong_khoang(a, b):
    result = []
    for x in range(max(2, a), b + 1):
        if la_so_hoan_hao(x):
            result.append(x)
    return result


def menu():
    while True:
        print("\n=== MENU CHƯƠNG TRÌNH ===")
        print("1. Kiểm tra số hoàn hảo")
        print("2. Liệt kê số hoàn hảo trong khoảng [a, b]")
        print("3. Liệt kê số nguyên tố trong khoảng [a, b]")
        print("4. Tính tổng a + b")
        print("0. Thoát")
        choice = input("Chọn chức năng: ")

        if choice == '1':
            n = int(input("Nhập số n: "))
            if la_so_hoan_hao(n):
                print(f"{n} là số hoàn hảo")
            else:
                print(f"{n} không phải số hoàn hảo")
        elif choice == '2':
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            if a > b:
                a, b = b, a
            ket_qua = so_hoan_hao_trong_khoang(a, b)
            if ket_qua:
                print(f"Các số hoàn hảo trong khoảng [{a}, {b}] là: {ket_qua}")
            else:
                print(f"Không có số hoàn hảo trong khoảng [{a}, {b}].")
        elif choice == '3':
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            if a > b:
                a, b = b, a
            ket_qua = tim_so_nguyen_to(a, b)
            if ket_qua:
                print(f"Các số nguyên tố trong khoảng [{a}, {b}] là: {ket_qua}")
            else:
                print(f"Không có số nguyên tố trong khoảng [{a}, {b}].")
        elif choice == '4':
            a = float(input("Nhập a: "))
            b = float(input("Nhập b: "))
            print(f"Tổng a + b là: {tinh_tong(a, b)}")
        elif choice == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == '__main__':
    menu()
