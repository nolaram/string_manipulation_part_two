# ask user for his/her name
user_name = str(input("Enter your name: "))

# convert the input to lower case characters
lower_case = ""

for char in user_name:
    if "A" <= char <= "Z":
        lower_case += chr(ord(char) + 32)
    else:
        lower_case += char

# print the output
print(lower_case)