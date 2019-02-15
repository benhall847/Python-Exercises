width = int(input("Width? "))
height = int(input("Height? "))
counter = 0
while counter < height:
    counter += 1
    if counter > 1 and counter < height:
        spacing = width - 2
        stars = 1
    else:
        stars = width -1
        spacing = 0
    print(('*' * stars) + (' ' * spacing) + '*')