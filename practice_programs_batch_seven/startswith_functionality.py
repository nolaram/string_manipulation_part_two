# ask user for his/her name
user_name = str(input("Enter your name: "))

# set a variable with the prefix that you want to find
starts_with = "Mar"

# find the prefix in the input
position = user_name.find(starts_with)

# if the input startswith the variable given
if position == 0:
    # print true
    print("True")

# if not
else:
    # print false
    print("False")