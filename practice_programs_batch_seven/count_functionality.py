# ask user for his/her name
user_name = str(input("Enter your name: "))

# set the variable with a value "a"
letter = "a"

# check how many times the variable appears
# set count to 0
count = 0

# for loop to check every character in input
for character in user_name:
    if character == letter:
        # increase count by 1 every time the character matches the variable
        count += 1

# print the output
print(count)