letters = {
    
}
user_input = input('Please enter a word: ')
for each_letter in user_input:
    letters[each_letter] = 0
for eachletter in user_input:
    if eachletter in letters:
        letters[eachletter] += 1
print(letters)