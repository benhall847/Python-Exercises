numbers = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
newList = []
for i in numbers:
    if i not in newList:
        newList.append(i)
print(newList)