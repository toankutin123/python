def tim_so_nguyen_to(n):
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

# Test
n = int(input("Nhập số nguyên n: "))
print("Các số nguyên tố từ 1 đến", n, "là:", tim_so_nguyen_to(n))
