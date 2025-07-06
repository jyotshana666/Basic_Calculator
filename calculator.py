# Basic Calculator Program
# This program performs basic arithmetic operations and some advanced mathematical functions.   

import math
def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    if num2 == 0:
        return "Error! Cannot divide by zero."
    return num1 / num2

def square_root(num):
    if num < 0:
        return "Error! Cannot calculate square root of a negative number."
    return math.sqrt(num)

def power(num1, num2):  
    return math.pow(num1, num2)

def logarithm(num):
    if num <= 0:
        return "Error! Logarithm of non-positive number is undefined."
    return math.log(num)

def natural_log(num):
    if num <= 0:
        return "Error! Natural logarithm of non-positive number is undefined."
    return math.log(num, math.e)

def sine(num):
    return math.sin(math.radians(num))

def cosine(num):
    return math.cos(math.radians(num))

def tangent(num):
    return math.tan(math.radians(num))

def factorial(num):
    if num < 0:
        return "Error! Factorial of negative number is undefined."
    return math.factorial(num)

def exponential(num):
    return math.exp(num)

# Menu driven Program 
def menu():
    print("\tBASIC CALCULATOR")
    print("\t----------------")
    print("\tOperations to perform")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square Root (√)")
    print("6. Power (^)")
    print("7. Log (base 10)")
    print("8. Natural Log (ln)")
    print("9. Sine (degrees)")
    print("10. Cosine (degrees)")
    print("11. Tangent (degrees)")
    print("12. Factorial")
    print("13. Exponential (e^x)")
    print("0. Exit")
while True:
    # Enter the choice to be perform operation 
    menu
    choice = input("Enter value(1-13):")
    # Entering two inputs from user
    print("\n")
    print("You have selected option:", choice)
    try:
        if choice == '0':
            print("Exiting Calculator. Goodbye!")
            break
        elif choice in ['1', '2', '3', '4', '5']:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            if choice == '1':
                print("Result:", add(x, y))
            elif choice == '2':
                print("Result:", subtract(x, y))
            elif choice == '3':
                print("Result:", multiply(x, y))
            elif choice == '4':
                print("Result:", divide(x, y))
            elif choice == '5':
                print("Result:", power(x, y))
        elif choice in ['6', '7', '8', '9', '10', '11', '12', '13']:
            x = float(input("Enter number: "))
            if choice == '6':
                print("Result:", square_root(x))
            elif choice == '7':
                print("Result:", logarithm(x))
            elif choice == '8':
                print("Result:", natural_log(x))
            elif choice == '9':
                print("Result:", sine(x))
            elif choice == '10':
                print("Result:", cosine(x))
            elif choice == '11':
                print("Result:", tangent(x))
            elif choice == '12':
                print("Result:", factorial(x))
            elif choice == '13':
                print("Result:", exponential(x))
        else:
            print("Invalid input")
    except Exception as e:
        print("Error:", e)

