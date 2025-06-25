print("Hello World")

greet = "This is a function that is saying hello"
print(greet)

# Type Checking 

one = "Bonjour"
two = 1234567890
three = True
 
print(f"This is a {type(one)}, I am a {type(two)} and finally I am a {type(three)}")

# String manipulation 

str_one = "Hi My Name Is Patricia."
multiple_str = str_one * 10 
upper_str = str_one.upper()
capital_str = str_one.capitalize()
capital_each_word = str_one.title()
find_letter_index = str_one.find("M")
print(find_letter_index)


## Free Code Camp 

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())  ## Finds the h in hello World in our alphabet varieble
print(index)
shifted = alphabet[index + shift ]  ### Square brackets finds the letter at a certain index. Find gets us said index 
print(shifted) 

# Loops and iterations
# A loop allows you to systematically go through a sequence of elements and execute actions on each one.
# Example Code
# for i in text:
# for is the keyword denoting the loop type. i is a variable that sequentially takes the value of the elements in text. The statement ends with a colon, :.

# Python relies on indentation to indicate blocks of code. A colon at the end of a line is a signal that a new indented block of code will follow.
# So, when no indented block is found after the final colon, the code execution stops and an IndentationError is thrown

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text:
    index = alphabet.find(char)  #This will get the index of the letters in text in alphabet
    print(char, index)  #Remeber -1 means (NOT FOUND!) 

# Strings are immutable, which means they cannot be changed once created. For example, you might think that the following code changes the value of my_string into the string 'train', but this is not valid:

# Example Code
# my_string = 'brain'
# my_string[0] = 't'

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    new_char = alphabet[new_index]  #Returns the new character which is three spaces in front of the current character 
    print('char:', char, 'new char:', new_char)


#Creating an empty value and then adding to it in your function is used to save your result. Thats why they do that. Rather than losing the answer for good in the great unknown.

# a += b
# The addition assignment operator enables you to add a value to a variable and then assign the result to that variable.


# Comparison operators allow you to compare two objects based on their values. You can use a comparison operator by placing it between the objects you want to compare. They return a Boolean value — namely True or False — depending on the truthfulness of the expression.

# Python has the following comparison operators:

# Operator	Meaning
# ==	Equal
# !=	Not equal
# >	Greater than
# <	Less than
# >=	Greater than or equal to
# <=	Less than or equal to

if x != 0:
    print(x) # This is the format of an if statement
