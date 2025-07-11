"""
Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

"""

# Multi Words Variable Names
myVariableName = "John"  # Camel Case 
MyVariableName = "John"  # Pascal Case 
my_variable_name = "John" # Snake Case



# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# ----------------------------------------------------- 
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)  #==> Python is awesome

# or /

x = "Python "
y = "is "
z = "awesome"
print(x + y + z) #==> Python is awesome


# Global Variables
# Global variables can be used by everyone, both inside of functions and outside.
"""
If you create a variable with the same name inside a function, 
this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, global and with the original value.
"""

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# The global Keyword
"""
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
"""

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


