"""
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:
"""

#! Multiline Strings

#? You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#? Note: in the result, the line breaks are inserted at the same position as in the code.

print('\n --------------------------------------------------')

#! Strings are Arrays

b = "hello world"
print(a[2])

print('\n --------------------------------------------------')

#! Looping Through a String
#? Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
    print(x)

print('\n --------------------------------------------------')

#! String Length
c = "hello world"
print(len(c))

#? The len() function returns the length of a string:

print('\n --------------------------------------------------')

#! Check String
#? To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt) #return True if the text is on the phrase txt 

print('\n --------------------------------------------------')

#! Check if NOT
#? To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("exprensive" not in txt)





