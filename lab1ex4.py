perfect_number= int(input("Enter a number:"))
divisors = []
for i in range(1, perfect_number):
    if perfect_number % i == 0:
        divisors.append(i)
if sum(divisors) == perfect_number:
    print(f"{perfect_number} is a perfect number")
else:
    print(f"{perfect_number} is not a perfect number")