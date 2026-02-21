# Program 1: Print 1 to n

n=int(input("Enter the last number you want to print up to:"))

for i in range(1, n+1):
    print(i)

#===============================
# Program 2: Even Numbers 1 to n


n=int(input("Enter the last number up to which you want to print even numbers:"))

for i in range(1, n+1):
    if i % 2 == 0:
        print(i)

# ==============================
# Program: Prime Number Checker


try:
    num = int(input("Enter the number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    raise SystemExit

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

n = int(input("Enter a number: "))

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

n = int(input("Enter value of N: "))

total = 0
for i in range(1, n + 1):
    total += i

print(f"Sum of digits from 1 to {n} is:", total)

# ==============================
# Program 6: Reverse a Number


num = int(input("Enter a number: "))

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














        
        