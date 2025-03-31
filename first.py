print("hello")
a=1
b=8
c=a=+b
print(c)



print("python".isalpha())

print("python".isascii())

print("500".isdecimal())

print("500".isdigit())

print("variable".isidentifier())

print("python".islower())

print("500".isnumeric())

print("python".isprintable())

print(" ".isspace()) 

print("Python".istitle()) 

print("PYTHON".isupper()) 

print("python".islower()) 

print("-".join(["a", "b", "c"]))

print("python".lower())

print("python".upper())

print(" python".lstrip())

try: 
    a = int(input("Enter first number: ")) 
    b = int(input("Enter second number: ")) 
    result = a / b 
    print("Result:", result) 
except ZeroDivisionError: 
    print("Cannot divide by zero!") 
except ValueError: 
    print("Invalid input! Please enter a number.") 