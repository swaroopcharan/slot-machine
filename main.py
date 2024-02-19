from deposit import deposit
from spin import spin

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Spin the slot machine? (Y/N): ")
        if answer == "N" or answer == "n":
            break
        elif answer == "Y" or answer == "y":
            balance += spin(balance)
        else:
            print("Give a correct command")

    print(f"Your final balance is ${balance}")

main()