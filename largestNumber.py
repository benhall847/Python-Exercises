numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def largestNum(x):
    largest = 0
    for i in x:
        if i > largest:
            largest = i
    return largest
print(largestNum(numbers))