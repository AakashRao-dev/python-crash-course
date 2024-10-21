# Programs on basic control structure & loops

# 1. if-else
age = int(input('Enter your age...\n'))
if (age > 18):
    print('You can drive :)')
else:
    print(f'You need to wait {18 - age} years!')

# 2. while loop
count = 1
while count <= 5:
    print(count)
    count += 1

# 3. For Loop
# Calculate sum from 1 to 10
sum = 0
for i in range(1, 11):
    sum += i
print('Total Sum:', sum)

# 4. Nested Loop
# print a patter of stars

n = 5
for i in range(1, n):
    for i in range(i):
        print("*", end="")
    print()

# Reverse Order
for i in range(n, 0, -1):
    for i in range(i):
        print("*", end="")
    print()

# 5. Break & Continue
# Program to find first even number and continue to number if odd
numbers = [7, 12, 5, 8, 3, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"The first even number in the list is {num}")
        break
    else:
        continue

# 6. Switch Case

# Program to implement simple switch case using a dictionary


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


choice = input("Enter operation (+, -, *, /): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operations = {
    '+': add(num1, num2),
    '-': subtract(num1, num2),
    '*': multiply(num1, num2),
    '/': divide(num1, num2),
}

if choice in operations:
    print(f"Result: {operations[choice]}")
else:
    print('Invalid Operator')
