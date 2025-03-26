# ask user to input with spaces in the beginning
user_input = str(input("Enter a character with spaces in the beginning: "))

# remove the spaces in the beginning without using lstrip
user_input = user_input.replace(" ", "")

# print the output
print(user_input)