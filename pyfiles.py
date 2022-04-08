#from sympy import symbols, Eq, solve
import os
clear = lambda: os.system('cls')


clear()
print('Calculator v1.2')
print("")
print('This is still a rudimentary build.')
print("")
print("")

while True:

	print("State option: ")
	print("")

	operation = int(input("1. Regular Operations \n2. Algebraic Expression \n>  "))
	print("")

	

	if operation == 1:

		equation = input("Enter Operation: \n>")
		ans = eval(equation)
		print("ans = ", ans)
		input("")
		clear()

	elif operation == 2:
		expr = input("Enter Operation (eg 2*x + 6): ")
		x = int(input("Value for x: "))
		ans = eval(expr)
		print("ans = ", ans)
		input("")
		clear()

	else:
		print("error: Select a valid option!")
		input("")
		clear()
		continue