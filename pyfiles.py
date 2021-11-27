def add(x, y):
	return x + y
def subtract(x, y):
	return x - y
def multiply(x, y):
	return x * y
def divide(x, y):
	return x / y

print('Calculator v0.1')

num1 = int(input('Enter Number: '))
num2 = int(input('Enter second number: '))
op = int(input('What would you like to do (Add/1, Subtract/2, multiply/3, divide/4): '))


def operator(x, z, y):
	print(num1, z , num2,'= ',y(num1, num2))

if op == 1:
	operator(op, '+', add)
if op == 2:
	operator(op, '-', subtract)
if op == 3:
	operator(op, '*', multiply)
if op == 4:
	operator(op, '/', divide)

input("")