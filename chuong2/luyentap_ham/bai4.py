def tim_so_nguyen_to(a, b):
    primes = []
    start = max(2, a)
    for i in range(start, b+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

# Nhập a và b
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("Các số nguyên tố trong khoảng [", a, ",", b, "] là:", tim_so_nguyen_to(a, b))
