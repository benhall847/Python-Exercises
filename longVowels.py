phrase = "Cats love fast vacuums"
newPhrase = ""
index = 0
translation = ''
leet = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'I', 'o', 'u']
l337 = ['AAAAA', 'EEEEE', 'IIIII', 'OOOOO', 'UUUUU', 'aaaaa', 'eeeee', 'iiiii', 'ooooo', 'uuuuu']

for letter in phrase:
    if letter in leet:
        if phrase[index] == phrase[index+1]:
            translation += (l337[leet.index(letter)] )
        else:
            translation += letter
    if letter not in leet:
        translation += letter
    index += 1
print(translation)