height = int(input("Height?"))
counter = 0
spacing = height
stars = 1
while counter != height:
    print((' ' * spacing) + ('*' * stars))
    counter += 1
    spacing -= 1
    stars += 2