def deposit():
    while True:
        amount = input("Enter amount to deposit(In USD): $")
        if amount.isdigit():
            amount = float(amount)
            if amount > 0:
                break
            else:
                print("Enter Valid Amount")
        else:
            print("Enter Valid Amount")
    return amount