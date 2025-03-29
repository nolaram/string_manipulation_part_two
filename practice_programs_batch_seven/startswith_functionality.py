# ask user for his/her name
user_name = str(input("Enter your name: "))

# set a variable with the prefix that you want to find
starts_with = "Mar"

# find the prefix in the input
position = starts_with.find(user_name)

# if the input startswith the variable given
    # print true
# if not
    # print false