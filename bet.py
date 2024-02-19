MIN_BET = 1
MAX_BET = 100

def get_bet():
    while True:
        bet = input("Enter bet amount on each line: $")
        if bet.isdigit():
            bet = float(bet)
            if bet > MIN_BET and bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter a Valid Number")
    return bet