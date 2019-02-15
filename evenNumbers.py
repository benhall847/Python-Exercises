numbers = str(input("Enter list of numbers, seperated by commas "))
numberList = numbers.split(' ')
new_list = []
for num in numberList:
    new_list.append(int(num))
even = []
for num in new_list:
    if num % 2 == 0:
        even.append(num)
print(even)