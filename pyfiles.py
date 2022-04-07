print('Calculator v1.1')
print('This is still rudimentary, but I plan on making this BIG B)')
while True:

	print("State option: ")
	operation = int(input("1. Integers with basic operations \n"))

	if operation == 1:

		equation = input("Enter Operation: ")
		ans = eval(equation)
		print("ans = ", ans)
		input("")