# ask user to input his/her name and with spaces after
user_name = str(input("Enter your name: "))

# remove the spaces without rstrip
user_name = user_name.replace(" ", "")

# print the output
print(f'"{user_name}"')