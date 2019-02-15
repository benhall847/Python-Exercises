response = "yes"
coins = 0
while response == "yes":
    print("You have %s coins." % (coins,))
    response = input("Do you want another? ")
    coins += 1
print("Bye")