numbers = [1, 2, 3, 4, 5, 6]
numbers2 = [1, 2, 3, 4, 5, 6]
index = 0
answer = []
for i in numbers:
    answer.append(i * numbers2[index])
    index += 1
print(answer)