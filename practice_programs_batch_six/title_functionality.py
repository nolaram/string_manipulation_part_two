# ask user for his/her name but with wrong inputs
user_name = str(input("Enter your name: "))

# split the input into words
user_name = user_name.split()

# capitalize the words
swap_case = [word[0].upper() + word[1:].lower() for word in user_name]

# add space
add_space = " ".join(swap_case)

# print output