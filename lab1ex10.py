def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
num = 28
print("Divisors of", num, "are:", get_divisors(num))