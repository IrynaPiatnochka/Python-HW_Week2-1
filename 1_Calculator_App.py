# Function to add two numbers
def add(a, b):
    return a + b
 
# Function to subtract two numbers
def subtract(a, b):
    return a - b
 
# Function to multiply two numbers
def multiply(a, b):
    return a * b
 
# Function to divide two numbers
def divide(a, b):
    return a / b
 
print("Select an operation.")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
 
 
# Take input from the user
enter = int(input("Select operations form 1, 2, 3, 4 : "))
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
 
if enter == 1:
    print(num_1, "+", num_2, "=",
                    add(num_1, num_2))
 
elif enter == 2:
    print(num_1, "-", num_2, "=",
                    subtract(num_1, num_2))
elif enter == 3:
    print(num_1, "*", num_2, "=",
                    multiply(num_1, num_2))
 
elif enter == 4:
    if num_2 == 0:
       print("Denominator is zero")

    else:
        print(num_1, "/", num_2, "=",
                    divide(num_1, num_2))

else:
   print("Invalid input")

