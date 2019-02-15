numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9]
def smallestNum(x):
    smallest = x[0]
    for i in x:
        if i < smallest:
            smallest = i
    return smallest
print(smallestNum(numbers))