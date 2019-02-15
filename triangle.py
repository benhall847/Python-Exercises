height = 4
counter = 0
spacing = 3
stars = 1
while counter != height:
    print((' ' * spacing) + ('*' * stars))
    counter += 1
    spacing -= 1
    stars += 2