def factorial(number):
	print(f"calculating factorial of {number}")
	result = 1
	for value in range(2, number + 1):
		result *= value
	print(f"Factorial of {number} is {result}")
	return result