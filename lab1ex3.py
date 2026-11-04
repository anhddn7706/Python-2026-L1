prime_number = int(input("Enter a number:"))
is_prime = True
if prime_number > 1:
    for i in range(2, int(prime_number/2) + 1):
        if (prime_number % i) == 0:
            is_prime = False
            break
if is_prime:
    print(f"{prime_number} is a prime number")
else:
    print(f"{prime_number} is not a prime number")
