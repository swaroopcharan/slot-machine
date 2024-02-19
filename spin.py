from lines import get_lines
from bet import get_bet
from slot_machine import get_spin
from slot_machine import print_slot_machine
from winnings import check_winnings

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}



def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(
                f"You don't have enough balance to place this bet. Your current balance: {balance}")
        else:
            break
    print(
        f"You are bettings ${bet} on {lines} lines. Total bet is ${lines * bet}")
    
    slots = get_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)

    winnings = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    return winnings - total_bet