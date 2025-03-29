# ask user for his/her name
user_name = str(input("Enter your name: "))

# make a blank variable
upper_case = ""

# for loop to check every character in the input
for char in user_name:
    # if the character is lower case
    if "a" <= char <= "z":
        # change it to upper case
        upper_case += chr(ord(char) - 32)

    # if already upper case
    else:
        # no changes
        upper_case += char

# print the output
