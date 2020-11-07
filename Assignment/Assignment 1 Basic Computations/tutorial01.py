# Function to add two numbers 
def add(num1, num2): 
	if isinstance(num1, str) | isinstance(num2, str):
		return 0
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
	if isinstance(num1, str) | isinstance(num2, str):
		return 0
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
	if isinstance(num1, str) | isinstance(num2, str):
		return 0
	multiplication = num1 * num2
	return multiplication

# Function to divide two numbers 
def divide(num1, num2): 
	if isinstance(num1, str) | isinstance(num2, str):
		return 0
	if num2 == 0:
		division = 0
	else:
		division = num1 / num2
	return division
		
# Function to add power function
#You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2): #num1 ^ num2
	power = 1
	if isinstance(num1, str) | isinstance(num2, str):
		return 0
	if num2 % 1 == 0:
		if num2 > 0:
			while 1:
				power = multiply(power,num1)
				num2 = subtract(num2,1)
				if num2 == 0:
					break
		elif num2 < 0:
			while 1:
				power = divide(power,num1)
				num2 = add(num2,1)
				if num2 == 0:
					break
		else:
			power = 1
	else:
		power = 0
	return power
	
# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printGP(a, r, n): 
	gp=[]
	if isinstance(a, str) | isinstance(r, str) | isinstance(n, str):
		gp.append(0)
	elif n % 1:
		gp.append(0)
	elif n <= 0:
		gp.append(0)
	else:
		for i in range(int(n)):
			gp.append(multiply(a,power(r,i)))
	return gp 

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n): 
	ap=[]
	if isinstance(a, str) | isinstance(d, str):
		ap.append(0)
	elif n % 1:
		ap.append(0)
	elif n <= 0:
		ap.append(0)
	else:
		for i in range(int(n)):
			ap.append(add(a,multiply(d, i)))
	return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n): 
	hp=[]
	if isinstance(a, str) | isinstance(d, str):
		hp.append(0)
	elif n % 1:
		hp.append(0)
	elif n <= 0:
		hp.append(0)
	elif a == 0:
		hp.append(0)
	else:
		for i in range(int(n)):
			temp = add(divide(1,a),multiply(d, i))
			if temp == 0:
				hp.append(0)
			else:
				hp.append(divide(1,temp))
	return hp

