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
