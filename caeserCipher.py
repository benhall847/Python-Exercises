phrase = "Cats love fast vacuums"

lower = phrase.lower()
translation = ''
alphabet = "abcdefghijklmnopqrstuvwxyz "
cipher = "bcdefghijklmnopqrstuvwxyza "

for letter in lower:
    if letter in cipher:
        translation += cipher[alphabet.index(letter)]
print(translation)