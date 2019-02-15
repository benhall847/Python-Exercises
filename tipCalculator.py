def tipCalculator():
    start = True
    try:
        bill = float(input("Total bill? : "))
    except:
        print("Invalid input! Try again.")
        return tipCalculator()
    while start:
        service = str(input("Was the service good, fair, or bad? : ")).lower()
        if service == 'good':
            tip = float(bill) * .2
            start = False
        elif service == 'fair':
            tip = float(bill) * .15
            start = False
        elif service == 'bad':
            tip = float(bill) * .1
            start = False
        else:
            print("Invalid input!")
    start = True
    while start:
        try:
            split = int(input("Split how many ways? : "))
            start = False
        except:
            print("Invalid input!")
    total = bill + tip
    per_person = (total + tip) / split
    print("Tip amount : $%.2f\nTotal amount : $%.2f\nAmount per person : $%.2f" % (tip, total, per_person))
tipCalculator()