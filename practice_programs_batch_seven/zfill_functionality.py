# ask three numbers from the user
user_name = str(input("Enter three numbers: "))

# value of zero you want to add
value = 6

# fill the three numbers with zero in the beginning so it becomes six digits
# add space in the beginning depending on the value
space = " " * (value - len(user_name)) + user_name
# replace the spaces with zero
zfill = space.replace(" ", "0")

# print the output
print(zfill)