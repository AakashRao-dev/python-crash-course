# Programs on Basic Operators & File Operations (read-write)

# Arithmetic
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

# Comparison

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")
