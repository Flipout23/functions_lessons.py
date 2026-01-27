# Create Functions Practice #1
# Declare a function called greet, which every time it is called prints "Hello world!"

# You should only define the function, you should not call it later.


def greet():
    print("Hello world!")




# Create Functions Practice #2
# Declare a Function: Create a function called welcome that takes a person's name as an argument. This function should print "Welcome {name}!" whenever it is called.

# Create a Variable: Define a variable named name and store any name of your choice in it.
name = "Alice"
# Note: Only define the function and create the variable. Do not call the function afterwards.

def welcome(name):
    print(f"Welcome {name}!")




# Create Functions Practice #3
# Declare a function called square, that takes any number as an parameter, and each time it is called, it prints the square of that number on the screen (that is, the value to the second power).

# The name of the argument that this function must take is number. Create this variable and assign it any number.

# envoke it

# def square(num):
#     squared= num ** 2
#     return squared

# print(square(3))

number = 5
def square(number):
    print(number ** 2)
print(square(number))