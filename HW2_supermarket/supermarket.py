"""
NAME: Soohyun Choi
PENN ID: 79153361
STATEMENT OF WORK: I worked alone without help
"""

# import random module
import random

# unit price of a lottery ticket
constant_lottery_unit_price = 2

# unit price of an apple
constant_apple_unit_price = .99

# unit price of a can of beans
constant_canned_beans_unit_price = 1.58

# unit price of a soda
constant_soda_unit_price = 1.23

# the user has initial $5 for shopping
money = 5

# the user has spent $0 initially
money_spent = 0

# the amounts of lottery ticket, apples, cans of beans, and sodas the user has purchased
lottery_amount, apple_amount, canned_beans_amount, soda_amount = 0, 0, 0, 0

# lottery winnings
winnings = 0


# print a welcome message
print(f"""
Welcome to the supermarket! Here's what we have in stock:
- Lottery tickets cost ${constant_lottery_unit_price} each
- Apples cost ${constant_apple_unit_price} each
- Cans of beans cost ${constant_canned_beans_unit_price} each
- Sodas cost ${constant_soda_unit_price} each
""")

# print how much money the user has available
print(f"You have ${money} available")


# ask if the user wants to purchase a lottery ticket
lottery_answer = input(f"First, do you want to buy a ${constant_lottery_unit_price} lottery ticket for a chance at winning $2-$10? (y/n) ")

# if the user inputs y or Y, purchase lottery ticket
if lottery_answer.upper() == "Y":
    money_spent += constant_lottery_unit_price
    lottery_amount += 1

    # generate a random int from 0 to 2 to simulate 33% probability
    lottery_win = random.randint(0, 2)

    # if the int is 0, the user wins the lottery
    if lottery_win == 0:
        # generate a random int from 2 to 10 to calculate the user's winnings
        winnings = random.randint(2, 10)
        money_spent -= winnings
        print(f"Congrats! You won ${winnings}!")

    # if the int is 1 or 2, the user loses the lottery
    else:
        print("Sorry! You did not win the lottery.")

# if the user inputs anything else, purchase no lottery ticket
else:
    print("No lottery tickets purchased.")


# print how much money the user has available
print(f"\nYou have ${round(money - money_spent, 2)} available")

# ask if the user wants to purchase apples
apple_answer = input("Do you want to buy apple(s)? (y/n) ")

# if the user inputs y or Y, purchase apples
if apple_answer.upper() == "Y":
    try:
        # ask the user how many they want to buy and cast the input to an integer
        amount = int(input("How many apple(s) do you want to by? "))
        price = round(amount * constant_apple_unit_price, 2)
        print(f"The user wants to buy {amount} apple(s). This will cost ${price}.")

        # calculate the money the user will need to pay
        if money - money_spent >= price:
            money_spent += price
            apple_amount += amount
            print(f"The user has enough money. {amount} apple(s) purchased.")
        # if the user doesn't have enough money, print the message
        else:
            print("Not enough money! No apples purchased.")

    # catch the error if the input cannot be cast to an integer
    except ValueError:
        print("Numerical values only! No apples selected.")

# if the user inputs anything else, purchase no apples
else:
    print("No apples purchased.")


# print how much money the user has available
print(f"\nYou have ${round(money - money_spent, 2)} available")

# ask if the user wants to purchase cans of beans
canned_beans_answer = input("Do you want to buy can(s) of beans? (y/n) ")

# if the user inputs y or Y, purchase cans of beans
if canned_beans_answer.upper() == "Y":
    try:
        # ask the user how many they want to buy and cast the input to an integer
        amount = int(input("How many can(s) of beans do you want to by? "))
        price = round(amount * constant_canned_beans_unit_price, 2)
        print(f"The user wants to buy {amount} can(s) of beans. This will cost ${price}.")

        # calculate the money the user will need to pay
        if money - money_spent >= price:
            money_spent += price
            canned_beans_amount += amount
            print(f"The user has enough money. {amount} can(s) of beans purchased.")
        # if the user doesn't have enough money, print the message
        else:
            print("Not enough money! No cans of beans purchased.")

    # catch the error if the input cannot be cast to an integer
    except ValueError:
        print("Numerical values only! No cans of beans selected.")

# if the user inputs anything else, purchase no cans of beans
else:
    print("No cas of beans purchased.")


# print how much money the user has available
print(f"\nYou have ${round(money - money_spent, 2)} available")

# ask if the user wants to purchase sodas
soda_answer = input("Do you want to buy soda(s)? (y/n) ")

# if the user inputs y or Y, purchase sodas
if soda_answer.upper() == "Y":
    try:
        # ask the user how many they want to buy and cast the input to an integer
        amount = int(input("How many soda(s) do you want to by? "))
        price = round(amount * constant_soda_unit_price, 2)
        print(f"The user wants to buy {amount} soda(s). This will cost ${price}.")

        # calculate the money the user will need to pay
        if money - money_spent >= price:
            money_spent += price
            soda_amount += amount
            print(f"The user has enough money. {amount} soda(s) purchased.")
        # if the user doesn't have enough money, print the message
        else:
            print("Not enough money! No sodas purchased.")

    # catch the error if the input cannot be cast to an integer
    except ValueError:
        print("Numerical values only! No sodas selected.")

# if the user inputs anything else, purchase no sodas
else:
    print("No sodas purchased.")


# print the shopping information
print(f"""
Money left: ${round(money - money_spent, 2)}
Lottery ticket(s) purchased: {lottery_amount}
Lottery winnings: ${winnings}
Apple(s) purchased: {apple_amount}
Can(s) of beans purchased: {canned_beans_amount}
Soda(s) purchased: {soda_amount}
Good bye!
""")
