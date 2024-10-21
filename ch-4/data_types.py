# String data type

# Literal assignment
first = "Aakash"
last = "Rao"

print(type(first))  # <class 'str'>
print(type(first) == str)  # True
print(isinstance(first, str))  # True

print('=========')

# Constructor Function
pizza = str("Pepperoni")
print(type(pizza))  # <class 'str'>
print(type(pizza) == str)  # True
print(isinstance(pizza, str))  # True

# Concatenation
fullname = first + " " + last
print(fullname)
