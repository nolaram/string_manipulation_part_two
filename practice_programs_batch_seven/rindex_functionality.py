# ask user for his/her name
user_name = str(input("Enter your name: "))

# set a variable you want to find
letter = "a"

# set position to -1 
position = -1

# look for the position
for character in range(len(user_name) -1, -1, -1):
    if user_name[character] == letter:
        position = character
        break
    
# if found
    # print the position
# if not 
    # print none