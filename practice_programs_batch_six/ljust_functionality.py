# ask user for his/her name
user_name = str(input("Enter your name: "))

# assign how many spaces to add
space = 10

# add the spaces
add_space = user_name + " " * (space - len(user_name))

# print the output