# ask user for his/her name
user_name = str(input("Enter your name: "))

# remove the prefix "Mar" if it's in the input
if user_name.startswith("Mar"):
    user_name = user_name.replace("Mar", "")
    # print the output
    print(user_name)
    
# if not
    # print the output