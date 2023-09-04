"""
NAME: Soohyun Choi
PENN ID: 79153361
STATEMENT OF WORK: I worked alone without help
"""

import random

# prefix values
constant_lottery_unit_price = 2
constant_apple_unit_price = 0.99
constant_canned_beans_unit_price = 1.58
constant_soda_unit_price = 1.23

money = 5
money_spent = 0
winnings = 0

lottery_amount, apple_amount, canned_beans_amount, soda_amount = 0, 0, 0, 0


def handle_lottery(answer):
    global money_spent, lottery_amount, winnings
    if answer == "y" or answer == "Y":
        money_spent += constant_lottery_unit_price
        lottery_amount += 1
        lottery_win = random.randint(0, 2)
        if lottery_win == 0:
            winnings = random.randint(2, 10)
            money_spent -= winnings
            return f"Congrats! You won ${winnings}!"
        return "Sorry! You did not win the lottery."
    return "No lottery tickets purchased."


def handle_apple(answer):
    global money_spent, apple_amount
    if answer == "y" or answer == "Y":
        try:
            amount = int(input("How many apple(s) do you want to by? "))
            price = round(amount * constant_apple_unit_price, 2)
            print(f"The user wants to buy {amount} apple(s). This will cost ${price}.")
            if money - money_spent >= price:
                money_spent += price
                apple_amount += amount
                return f"The user has enough money. {amount} apple(s) purchased."
            return "Not enough money! No apples purchased."
        except ValueError:
            return "Numerical values only! No apples selected."
    return "No apples purchased."


def handle_canned_beans(answer):
    global money_spent, canned_beans_amount
    if answer == "y" or answer == "Y":
        try:
            amount = int(input("How many can(s) of beans do you want to by? "))
            price = round(amount * constant_canned_beans_unit_price, 2)
            print(f"The user wants to buy {amount} can(s) of beans. This will cost ${price}.")
            if money - money_spent >= price:
                money_spent += price
                canned_beans_amount += amount
                return f"The user has enough money. {amount} can(s) of beans purchased."
            return "Not enough money! No cans of beans purchased."
        except ValueError:
            return "Numerical values only! No cans of beans selected."
    return "No cas of beans purchased."


def handle_soda(answer):
    global money_spent, soda_amount
    if answer == "y" or answer == "Y":
        try:
            amount = int(input("How many soda(s) do you want to by? "))
            price = round(amount * constant_soda_unit_price, 2)
            print(f"The user wants to buy {amount} soda(s). This will cost ${price}.")
            if money - money_spent >= price:
                money_spent += price
                soda_amount += amount
                return f"The user has enough money. {amount} soda(s) purchased."
            return "Not enough money! No sodas purchased."
        except ValueError:
            return "Numerical values only! No sodas selected."
    return "No sodas purchased."


# intro
print("""
Welcome to the supermarket! Here's what we have in stock:
- Lottery tickets cost $2 each
- Apples cost $0.99 each
- Cans of beans cost $1.58 each
- Sodas cost $1.23 each
""")
print(f"You have ${money} available")


# shopping trip
lottery_answer = input("First, do you want to buy a $2 lottery ticket for a chance at winning $2-$10? (y/n) ")
print(handle_lottery(lottery_answer))

print(f"\nYou have ${round(money - money_spent, 2)} available")
apple_answer = input("Do you want to buy apple(s)? (y/n) ")
print(handle_apple(apple_answer))

print(f"\nYou have ${round(money - money_spent, 2)} available")
canned_beans_answer = input("Do you want to buy can(s) of beans? (y/n) ")
print(handle_canned_beans(canned_beans_answer))

print(f"\nYou have ${round(money - money_spent, 2)} available")
soda_answer = input("Do you want to buy soda(s)? (y/n) ")
print(handle_soda(soda_answer))


# results of shopping
print(f"""
Money left: ${round(money - money_spent, 2)}
Lottery ticket(s) purchased: {lottery_amount}
Lottery winnings: ${winnings}
Apple(s) purchased: {apple_amount}
Can(s) of beans purchased: {canned_beans_amount}
Soda(s) purchased: {soda_amount}
Good bye!
""")
