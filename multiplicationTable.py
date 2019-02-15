number1 = 1
multiply = 0
while number1 <= 10:
    multiply += 1
    print("%d X %d = %d" % (number1, multiply, (number1 * multiply)))
    if multiply == 10:
        number1 += 1
        multiply = 0