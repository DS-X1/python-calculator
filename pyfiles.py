def add(x, y):
	return x + y
def subtract(x, y):
	return x - y
def multiply(x, y):
	return x * y
def divide(x, y):
	return x / y



print('Calculator v1.0.3')
print('This is still rudimentary, but I plan on making this BIG B)')
while True:
	num1 = int(input('Enter Number: '))
	op = int(input('Would you like to Add(1), Subtract(2), Multiply(3), Divide(4): '))
	num2 = int(input('Enter second number: '))


	def operator(x, y):
		print(num1, x , num2,'= ',y(num1, num2))

	if op == 1:
		operator(op, '+', add)
	if op == 2:
		operator(op, '-', subtract)
	if op == 3:
		operator(op, '*', multiply)
	if op == 4:
		operator(op, '/', divide)

	input("")