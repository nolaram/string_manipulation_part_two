# ask user for his/her name but with wrong inputs
user_name = str(input("Enter your name: "))

# convert casing
words = [user_name[0]]

for char in user_name [1:]:
    if char.isupper():
        words.append(" " + char)
    else:
        words[-1] += char

# add space and capitalize
add_space = " ".join(word.capitalize() for word in words)