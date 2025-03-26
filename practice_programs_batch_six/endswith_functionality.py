# ask user for his/her name
user_name = str(input("Enter your name: "))

# check if his/her name ends with "lon"
ends_with = "lon"

position = user_name.find(ends_with)

# if name ends with lon
if position != -1 and position == len(user_name) - len(ends_with):
    # print True
    print("True")
# if not
else:
    # print False
    print("False")