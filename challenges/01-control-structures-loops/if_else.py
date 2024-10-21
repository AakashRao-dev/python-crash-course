from datetime import date
# ============= Challenge 1: Odd or Even =============
# Write a program that takes an integer input from the user and prints whether the number is odd or even using if -else .

num = float(input("Enter a number: "))
if num % 2 == 0:
    print(f'The number {num} is even')
else:
    print(f'The number {num} is odd')

# =========================================================
# ============= Challenge 2: Grade Calculator =============
# Create a program that takes a student's score as input and outputs their grade based on the following scale:

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

score = int(input('Enter your score between 0 to 100: '))

# Approach-A
if score in range(90, 100 + 1):
    print('A')
elif score in range(80, 90 + 1):
    print('B')
elif score in range(70, 80 + 1):
    print('C')
elif score in range(60, 70 + 1):
    print('D')
elif score in range(0, 60 + 1):
    print('F')

# Approach-B
if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 90:
    print('B')
elif 70 <= score <= 80:
    print('C')
elif 60 <= score <= 70:
    print('D')
elif 0 <= score <= 60:
    print('F')

# ========================================================
# ================ Challenge 3: Leap Year ================
# Write a program that checks if a given year is a leap year or not. A year is a leap year if:

# It is divisible by 4 but not divisible by 100, or
# It is divisible by 400.

current_date = date.today()
print(current_date)
current_year = current_date.year
print(current_year)

if current_year % 4 == 0 and current_year % 100 != 0:
    print('This is a leap year')
else:
    print('Sorry, this isn\'t a leap year')
