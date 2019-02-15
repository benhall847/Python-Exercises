phrase = "Cats love fast vacuums"

upper = phrase.upper()
translation = ''
leet = ['A', 'E', 'G', 'I', 'O', 'S', 'T']
l337 = ['4', '3', '6', '1', '0', '5', '7']

for letter in upper:
    if letter in leet:
        translation += l337[leet.index(letter)]
    if letter not in leet:
        translation += letter
print(translation)