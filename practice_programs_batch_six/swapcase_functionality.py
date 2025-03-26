# ask user for his/her name
user_name = str(input("Enter your name: "))

# convert the casing 
swap_case = ""

for char in user_name:
    if "a" <= char <= "z":
        swap_case += chr(ord(char) - 32)
    elif "A" <= char <= "Z":
        swap_case += chr(ord(char) + 32)
    else:
        swap_case += char

# print the output