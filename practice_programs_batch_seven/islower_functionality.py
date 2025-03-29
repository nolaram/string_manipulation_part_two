# ask user for his/her name
user_name = str(input("Enter your name: "))

# make a variable that has a value of true
lower = True

# for loop to check every character
for character in user_name:
    # if one character is upper case
    if "A" <= character <= "Z":
        # change the variable into false
        lower = False
        # stop the program
        break

# if all lower case
if lower == True:
    # print true
    print("True")
    
# if not
    # print false
