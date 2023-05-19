import random


MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_value={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_count={
    "A":10,
    "B":8,
    "C":4,
    "D":2
}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_check=column[line]
            if symbol != symbol_check:
                break
        else:
            winnings+= values[symbol]*bet
            winning_lines.append(line+1)
    return winnings,winning_lines

def slot_spin_go(rows,cols,symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns=[]
    for col in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end="|")
            else:
                print(column[row],end='')
        print()

def deposit():
    while True:
        amount = input("Amount of deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter a number")

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on(1-" + str(MAX_LINES)+")?")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINES:
                return lines
            else:
                print(f"Amount must be between 1 and {MAX_LINES}")
        else:
            print("Please enter a number")

def get_bet():
    while True:
        amount = input("Amount of bet: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}")
        else:
            print("Invalid input. Please enter a number.")

def main():
    balance=deposit()
    lines=get_number_of_lines()
    MAX_BET=balance
    MIN_BET=balance*0.25
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet>balance:
            print(f"Insufficient funds. Your balance is ${balance}")
        else:
            break
    total_bet=bet*lines
    print(f"You are betting ${bet} on {lines}. Total bet is equal to ${total_bet}")
    slots=slot_spin_go(ROWS,COLS,symbol_count)
    print_slot(slots)
    winnings,winning_lines=check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}.")
