# ask user for his/her name
user_name = str(input("Enter your name: "))

# check if the input is all uppercase
upper = True

for char in user_name:
    if "a" <= char <= "z":
        upper = False
        break

# if all uppercase
if upper == True:
    # print True
    print("True")
# if not
else:
    # print False
    print("False")