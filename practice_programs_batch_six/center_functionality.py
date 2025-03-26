# ask user for his/her name
user_name = str(input("Enter your name: "))

# assign a value for the desired space
space = 10

# seperate the space
white_space = max(0, space - len(user_name))
left_space = white_space // 2
right_space = white_space - left_space

# add the space 
# print output