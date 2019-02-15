user_input = int(input("A number between 1 and 20 : "))
import time
while user_input != -1:
    if user_input > 20:
        break
    print(user_input)
    user_input -= 1
    time.sleep(1)
print("BLAST OFF!")