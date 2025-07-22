def add (a ,b) :
	return a+b
def subtract (a ,b) :
	return a-b
def multiply (a ,b) :
	return a*b
def divide (a ,b) :
	if b != 0 :
		return a/b
	else :
		return "can't divide by zero !!"
print("welcome to basic calculator")
num1 = float(input("Enter your first number: "))
op = input("select +,-,*or/ : ")
num2 = float(input("Enter your second number:  "))
if op == "+" :
	print("ANS= " ,add(num1 ,num2))
elif op == "-" :
	print("ANS= " ,subtract(num1 ,num2))
elif op == "*" :
	print("ANS= " ,multiply(num1 ,num2))
elif op == "/" :
	print("ANS= " ,divide(num1 ,num2))
else :
	print("select your operator carefully!!")
print("Thanks for using it ")