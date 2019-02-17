words = {
    
}
user_input = input('Please enter a word: ')

seperateWords = user_input.split(' ')

for each_word in seperateWords:
    if each_word not in words:
        words[each_word] = 0

for eachWord in seperateWords:
    if eachWord in words:
        words[eachWord] += 1
        
print(words)