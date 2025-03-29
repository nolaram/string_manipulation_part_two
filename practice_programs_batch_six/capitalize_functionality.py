# ask user for his/her name
user_name = str(input("Enter your name: "))

# capitalize the casing
capitalize = []


if user_name:
    output = user_name[0].upper() + user_name[1:].lower()
else:
    output = ""

# print the output