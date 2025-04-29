# This is a Basic Calculator app that contains basic functions such as addition , subtraction , multiplication and Division of two numbers.
# This is a addition function
def addition(num1,num2):
    return num1 + num2

# This is a subtraction function
def subtraction(num1,num2):
    return num1 - num2

# This is a multiplication function
def multiplication(num1,num2):
    return num1 * num2

# This is a divivsion function
def division(num1,num2):
    if num2 == 0:
        return "Error! Cannot divide by zero."
    return num1 / num2

# Menu driven Program 
print("\tBASIC CALCULATOR")
print("\t----------------")
print("\tOperations to perform")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Exit")

# Enter the choice to be perform operation 
choice = int(input("Enter value(1-5):"))

# Entering two inputs from user
n1 = eval(input("Enter the first value:"))
n2 = eval(input("Enter the second value:"))

if choice == 1 :
    print("Addition of {} and {} is {}".format(n1,n2,addition(n1,n2)))
elif choice == 2:
    print("Subtraction of {} and {} is {}".format(n1,n2,subtraction(n1,n2))) 
elif choice == 3:
    print("Multiplication of {} and {} is {}".format(n1,n2,multiplication(n1,n2)))
elif choice == 4:
    print("Division of {} and {} is {}".format(n1,n2,division(n1,n2)))
elif choice == 5:
    print("Exit")
else: 
    print("Invlaid input")