# the phrase I want to translate/cipher
phrase = input("A phrase to translate : ")

# create lower-case version of phrase
lower_phrase = phrase.lower()

# my alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz "

# a letter cipher (alphabet shifted by one)
letter_cipher = "bcdefghijklmnopqrstuvwxyza "

# a number cipher (the position of each letter in the alphabet)
number_cipher = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21',
    '22',
    '23',
    '24',
    '25',
    '26'
]

letter_cipher2 = "efghijklmnopqrstuvwxyzabcd "


def decode(your_phrase, your_cipher, your_alphabet):

    # call the map_over-function, with the given parameters.
    # call the translate-function within the map_over-function.
    return map_over(your_phrase, your_cipher, your_alphabet, translate)



def translate(letters, master_cipher, master_alphabet):
    
    # if the given cipher index has a number
    if master_cipher[master_alphabet.index(letters)][0] in "1234567890":

        # return the translation/cipher of the character, plus a space.
        return master_cipher[master_alphabet.index(letters)] + ' '
    
    # return the translation/cipher of the character
    return master_cipher[master_alphabet.index(letters)]



def map_over(the_phrase, the_cipher, the_alphabet, translate_fnctn):
    result = ''
    # for each character in the given phrase
    for ea_char in the_phrase:
        
        # if the character is in the given alphabet
        if ea_char in the_alphabet:
                
                # add the translation of each character to the result 
            result += translate_fnctn(ea_char, the_cipher, the_alphabet)
            
    # remove any extra spaces at the end of the result
    # return the results
    result.strip()
    return result

print(decode(lower_phrase, number_cipher, alphabet))

backwards_phrase = (input("Give me a phrase to decipher : "))

print(decode(backwards_phrase, alphabet, number_cipher))