#Program 1: Largest of Three Numbers

def largest_of_three():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print("Largest number is:", max(a, b, c))

#Program 2: Even or Odd

def even_or_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is Even Number")
    else:
        print(f"{num} is Odd Number")

#Program 3: Multiplication Table 

def multiplication_table():
    number = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number*i}")

#Program 4: Simple Calculator 

def simple_calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator from given list to perform operation on two numbers :(+, -, *, /) ")

    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Division by zero is not possible (undefined)")
    else:
        print("Invalid operator")


#All Program Execution menu 

while True:
    print("\n1. Largest of Three")
    print("2. Even or Odd")
    print("3. Multiplication Table")
    print("4. Simple Calculator")
    print("5. Exit")

    choice = input("enter Sr.no. of program you want to perform: ")

    if choice == "1":
        largest_of_three()
    elif choice == "2":
        even_or_odd()
    elif choice == "3":
        multiplication_table()
    elif choice == "4":
        simple_calculator()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")


