numbers = [
    [2, 3, 4], 
    [8, -2, 6]
]
numbers2 = [
    [8, 20, 6],
    [4, -7, 6]
]
matrix = [
    [],
    []
]
result = []
result2 = []
index = 0
sublength = len(numbers[0])

for i in numbers:
    for num in i:
        result.append(num)

for i in numbers2:
    for num in i:
        result2.append(num)

length = len(result)
for i in range(length):
    matrix[index].append(result[i] + result2[i])
    if len(matrix[index]) == sublength:
        index += 1
print(matrix)