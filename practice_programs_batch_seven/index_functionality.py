# ask user for his/her name
user_name = str(input("Enter your name: "))

# set the variable that you want to find in the input
letter = "a"

# set the position to -1 incase the letter is not found
position = -1

# look for the position where the variable first appears
for character in range(len(user_name)):
    if user_name[character] == letter:
        position = character
        break

# if the letter is found
if position != -1:
    # print the position
    print(position)

# if not
else:
    # print none
    print("The letter does not exist in the input")