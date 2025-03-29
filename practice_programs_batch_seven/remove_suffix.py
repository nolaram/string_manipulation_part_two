# ask user for his/her name
user_name = str(input("Enter your name: "))

# check if matches with the same suffix "lon"
# if yes
if user_name.endswith("lon"):
    # replace the suffix with blank
    user_name = user_name.replace("lon", "")
        # print the name
# if no
    # print the input without changes