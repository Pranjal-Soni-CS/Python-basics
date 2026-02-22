#alphanumeric remover program
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Program 1: Print 1 to n

def numbercount():
    n=get_int("Enter the last number you want to print up to:")
    
    for i in range(1, n+1):
        print(i)
    if n<=0:
        print(f"{n} is not a natural number.")
#===============================
# Program 2: Even Numbers 1 to n

def evennumber():
    n=get_int("Enter the last number up to which you want to print even numbers:")
    for i in range(2, n+1):
        if i % 2 == 0:
            print(i)
    
    if n<=1:
        print(f"Numbers less than 2 are not  even number.")
# ==============================
# Program: Prime Number Checker

def primenumber():
    num=get_int("enter the number")
    if num < 2:
        print(f"{num} is not a prime number")
    else:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")


# ==============================
# Program 4: Factorial

def factorial():
    n = get_int("Enter a number: ")

    if n < 0:
        print( "Factorial not defined for negative numbers")
    elif n == 0:
        print((f"Factorial of {n} is:{1}"))

    elif n>0:
        factorial = 1

        for i in range(1, n + 1):
            factorial *= i 
        print(f"Factorial of {n} is:{factorial}")


# ==============================
# Program 5: Sum of First N Natural Numbers

def sumnumbers():
    while True:
        n = get_int("Enter value of N: ")
        total = 0
        if n<0:
            print("enter positive numbers")
        else:    
            for i in range(1, n + 1):
                total += i

            print(f"Sum of digits till {n} is:", total)
        break

# ==============================
# Program 6: Reverse a Number

def reverse():
    num = get_int("Enter a number: ")
    sign = -1 if num < 0 else 1 #storing sign
    temp = abs(num)#makimg int positive if it is negative 

    reverse = 0
    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10

    result = reverse * sign

    print("Input Number:",num)
    print("Reversed Number:",result)

#Program Menu 
while True:
    print("======MENU======")
    print("1. Print 1 to n")
    print("2. Even Numbers 1 to n")
    print("3. Prime Number Checker")
    print("4. Factorial")
    print("5. Sum of First N Natural Numbers")
    print("6.Reverse a Number")
    print("0. Exit")
    
    choice=get_int("Enter your Choice:")
    
    if choice==1:
        numbercount()
    elif choice==2:
        evennumber()
    elif choice==3:
        primenumber()
    elif choice==4:
        factorial()
    elif choice==5:
        sumnumbers()
    elif choice==6:
        reverse()
    elif choice==0:
        print("Exiting Program.....")
        break
    else :
        print("Invalid Choice")