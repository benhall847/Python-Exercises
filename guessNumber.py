import random
play_again = "Y"
guesses_left = 5
while play_again == "Y":
    play_again == "N"
    print("I am thinking of a number between 1 and 10.")
    if guesses_left == 5:
        randomNumber = random.randint(1, 10)
    print("You have %s guesses left." % guesses_left)
    answer = int(input("What's the number? : "))
    if answer < randomNumber:
        print("%s is too low." % answer)
    elif answer > randomNumber:
        print("%s is too high." % answer)
    guesses_left -= 1
    if answer != randomNumber and guesses_left == 0:
        print("You ran out of guesses")
        play_again = input("Do you want to play again (Y or N)? ").upper()
        if play_again == "Y":
            guesses_left = 5
        else:
            break
    if answer == randomNumber:
        print("YEAH!!!")
        play_again = input("Do you want to play again (Y or N)? ").upper()
        if play_again == "Y":
            guesses_left = 5
        else:
            break