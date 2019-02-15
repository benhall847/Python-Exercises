user_input = input("Text? ")
counter = 0
length = len(user_input) + 4
print('*' * length)
while counter != 1:
    print('* ' + user_input + ' *')
    counter += 1
print('*' * length)