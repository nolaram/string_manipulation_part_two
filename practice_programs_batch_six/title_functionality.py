# ask user for input
user_name = str(input("Enter your name: "))
sentence = user_name.split()

# list to make things easier
upper = []

# convert first letter to uppercase and the rest to lower letters
for word in sentence:
    if word:
        upper.append(word[0].upper() + word[1:].lower())
        output = ''.join(upper)

# print the output
print(output)