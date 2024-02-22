# Slot Machine Simulation

This Python script simulates a basic slot machine game where users can spin the reels and potentially win based on the combination of symbols.

## Features

- Users can deposit money into their balance.
- Users can choose the number of lines to bet on.
- Users can place bets on each line.
- The slot machine spins and displays the results.
- Winnings are calculated based on the symbols' combinations.

## Prerequisites

- Python 3.x

## How to Use

1. Clone this repository to your local machine or download the `slot_machine.py` file.
2. Ensure you have Python installed on your system.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `slot_machine.py`.
5. Run the script by executing the command: `python slot_machine.py`.
6. Follow the on-screen prompts to play the game.

## Instructions

- When prompted, enter the amount of money you want to deposit.
- Choose the number of lines you want to bet on (1-3).
- Enter the bet amount for each line.
- Spin the slot machine by typing 'Y' or 'N' to continue or exit, respectively.
- After each spin, the results will be displayed, showing any winnings.
- The game continues until the user chooses to exit.

## Customization

- You can customize the symbols, their counts, and values by modifying the `symbol_count` and `symbol_value` dictionaries in the script.

## Example

```bash
$ python slot_machine.py
Enter amount to deposit(In USD): $100
Current balance is $100
Spin the slot machine? (Y/N): Y
Enter number of lines to bet on (1-3): 3
Enter bet amount on each line: $5
You are bettings $5.0 on 3 lines. Total bet is $15.0
A | B | D
C | D | B
B | C | A
You won $0.
Current balance is $85.0
Spin the slot machine? (Y/N): N
Your final balance is $85.0
```

## Credits

This code was written by Swaroop Charan Pasala.
Thank you for visiting this far. Hope you like my work.
