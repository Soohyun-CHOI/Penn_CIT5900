# TODO: Students, fill out statement of work header
# Student Name in Canvas: Soohyun Choi
# Penn ID: 79153661
# Did you do this homework on your own (yes / no): yes
# Resources used outside course materials: X

# import statements
from random import shuffle, randint


# TODO: Write the functions as described in the instructions

def get_user_input(question):
    """
    Prompt the user with 'question' and process the input.

    Args:
        question (str): question to get user input
    Returns:
        int | str: post-processed user input
    """
    answer = input(question)

    # remove leading and trailing whitespaces
    answer_strip = answer.strip()

    # if length is 0 (after removing whitespaces), reprompt
    if not answer_strip:
        get_user_input(question)

    try:
        # if the input is a number, cast and return an integer type
        return int(answer_strip)
    except ValueError:
        # if the input is a power card, return the power card as uppercase
        if answer_strip.upper() in ("SOH", "DOT", "DMT"):
            return answer_strip.upper()
        # if the input is any other str, return the str as lowercase
        return answer_strip.lower()


def setup_water_cards():
    """
    Create a shuffled list of water cards such that:
    30 cards of value 1, 15 cards of value 5, 8 cards of 10.

    Returns:
       list: water cards pile (list of integers)
    """
    # HINT: use shuffle func from random module
    water_cards_pile = [1 for _ in range(30)] + [5 for _ in range(15)] + [10 for _ in range(8)]
    shuffle(water_cards_pile)

    return water_cards_pile


def setup_power_cards():
    """
    Create a shuffled list of power cards such that:
    10 cards of SOH, 2 cards of DOT, 3 cards of DMT.

    Returns:
        list: power cards pile (list of strings)
    """
    # HINT: use shuffle func from random module
    power_cards_pile = ["SOH" for _ in range(10)] + ["DOT" for _ in range(2)] + ["DMT" for _ in range(3)]
    shuffle(power_cards_pile)

    return power_cards_pile


def setup_cards():
    """
    Set up both the water card and power card piles.

    Returns:
        2-tuple: (1) water cards pile, (2) power cards pile (list)
    """
    water_cards_pile = setup_water_cards()
    power_cards_pile = setup_power_cards()

    result = (water_cards_pile, power_cards_pile)
    return result


def get_card_from_pile(pile, index):
    """
    Remove the entry at the index of the pile.

    Args:
        pile (list): water cards pile or power cards pile
        index (int): index of the entry to remove from the pile
    Returns:
        int | str: entry at 'index' of the 'pile'
    """
    # remove the entry at the index of the pile & modify the pile by reference
    return pile.pop(index)


def arrange_cards(cards_list):
    """
    Arrange the players cards such that:
    (1) the first 3 indices are water cards, sorted in ascending order
    (2) the last 2 indices are power cards, sorted in alphabetical order.

    Args:
        cards_list (list): player's hand
    """
    cards_list.sort(key=str)
    cards_list.sort(key=lambda x: len(str(x)))


def deal_cards(water_cards_pile, power_cards_pile):
    """
    Deal card to player 1 and player 2 and arrange them.

    Args:
        water_cards_pile (list): water cards pile
        power_cards_pile (list): power cards pile
    Returns:
        2-tuple: (1) player 1's hand, (2) player 2's hand (list)
    """
    player_1_cards, player_2_cards = [], []

    # deal cards to player 1 and 2 (3 water, 2 power)
    # take off a card from the first entry in the pile
    for i in range(0, 3):
        player_1_cards.append(water_cards_pile.pop(0))
        player_2_cards.append(water_cards_pile.pop(0))

    for i in range(0, 2):
        player_1_cards.append(power_cards_pile.pop(0))
        player_2_cards.append(power_cards_pile.pop(0))

    # call arrange_cards func to arrange the cards
    arrange_cards(player_1_cards)
    arrange_cards(player_2_cards)

    result = (player_1_cards, player_2_cards)
    return result


def apply_overflow(tank_level):
    """
    If 'tank_level' >= 80, apply the overflow rule such that:
    remaining water = maximum fill value - overflow

    Args:
        tank_level (int): current water tank level
    Returns:
        int: overflow-applied tank level | starting tank level if no overflow occurred
    """
    return 160 - tank_level if tank_level > 80 else tank_level


def use_card(player_tank, card_to_use, player_cards, opponent_tank):
    """
    Get 'card_to_use' from the player's hand.
    Update the tank level and apply overflow if necessary.

    Args:
        player_tank (int): current player's water tank level
        card_to_use (int | str): card from user input
        player_cards (list): player's hand
        opponent_tank (int): opponent's water tank level
    Returns:
        2-tuple: (1) player's tank, (2) opponent's tank
    """
    # remove the card from player's hand
    player_cards.remove(card_to_use)

    # update the tank level
    if type(card_to_use) == int:
        player_tank += card_to_use
    elif type(card_to_use) == str:
        # steal half opponent's tank value
        if card_to_use == "SOH":
            steal = int(opponent_tank / 2)
            player_tank += steal
            opponent_tank -= steal
        # drain opponent's tank
        elif card_to_use == "DOT":
            opponent_tank = 0
        # double player's tank's value
        elif card_to_use == "DMT":
            player_tank *= 2

    result = (player_tank, opponent_tank)
    return result


def discard_card(card_to_discard, player_cards, water_cards_pile, power_cards_pile):
    """
    Discard 'card_to discard' from the player's hand.
    Return it to the last index of the pile.

    Args:
        card_to_discard (int | str): card from user input
        player_cards (list): player's hand
        water_cards_pile (list): water cards pile
        power_cards_pile (list): power cards pile
    """
    # discard the card from the player's hand
    player_cards.remove(card_to_discard)

    # return the card to its pile
    if type(card_to_discard) == int:
        water_cards_pile.append(card_to_discard)
    elif type(card_to_discard) == str:
        power_cards_pile.append(card_to_discard)


def filled_tank(tank):
    """
    Determine if 75 <= tank level <= 80.

    Args:
        tank (int): water tank level
    Returns:
        bool: True if the tank is filled, false otherwise
    """
    return 75 <= tank <= 80


def check_pile(pile, pile_type):
    """
    Check if 'pile' is empty.
    If so, replenish the pile by calling setup_cards function.

    Args:
        pile (list): cards pile
        pile_type (str): "water" | "power"
    """
    if not pile:
        pile += setup_water_cards() if pile_type == "water" else setup_power_cards()


def human_play(human_tank, human_cards, water_cards_pile, power_cards_pile, opponent_tank):
    """
    Get the user input and use or discard a card according to the input.
    Draw new card of the same type.
    Args:
        human_tank (int): human's water tank level
        human_cards (list): human's hand
        water_cards_pile (list): water cards pile
        power_cards_pile (list): power cards pile
        opponent_tank (int): computer's water tank level
    Returns:
        2-tuple: (1) human's water tank level, (2) computer's water tank level (int)
    """
    # show the human player's water level and then computer player's
    print(f"Your water level is at: {human_tank}")
    print(f"Computer's water level is at: {opponent_tank}")

    # show the human player's hand
    print(f"Your cards are: {human_cards}")

    while True:
        # ask human player if they want to use or discard a card.
        # if they enter an invalid answer, reprompt until it's valid
        answer = get_user_input("Do you want to use a card or discard a card? (u / d): ")
        if answer == "u":
            while True:
                # if they enter a card which is not in their hand, reprompt until it's valid
                card = get_user_input("Which card do you want to use?: ")
                if card in human_cards:
                    break
            # print the card the human player uses
            print(f"Playing with card: {card}")
            # use the card
            human_tank_update, computer_tank_update = use_card(human_tank, card, human_cards, opponent_tank)
            break
        elif answer == "d":
            while True:
                # if they enter a card which is not in their hand, reprompt until it's valid
                card = get_user_input("Which card do you want to discard?: ")
                if card in human_cards:
                    break
            # print the card the human player discards
            print(f"Discarding card: {card}")
            # discard the card
            discard_card(card, human_cards, water_cards_pile, power_cards_pile)
            human_tank_update, computer_tank_update = human_tank, opponent_tank
            break

    # handle overflows
    human_tank_update = apply_overflow(human_tank_update)

    # draw a new card of the same type they just used / discarded
    if type(card) == int:
        new = get_card_from_pile(water_cards_pile, 0)
        print(f"Drawing water card: {new}")
    else:  # type(card) == str
        new = get_card_from_pile(power_cards_pile, 0)
        print(f"Drawing power card: {new}")

    human_cards.append(new)
    # keep human's hand arranged after adding the new card
    arrange_cards(human_cards)

    # print the new tank value for the player and opponent
    print(f"Your water level is now at: {human_tank_update}")
    print(f"Computer's water level is now at: {computer_tank_update}")
    print(f"Your cards are now: {human_cards}")

    result = (human_tank_update, computer_tank_update)
    return result


def computer_play(computer_tank, computer_cards, water_cards_pile, power_cards_pile, opponent_tank):
    """
    Args:
        computer_tank (int): computer's water tank level
        computer_cards (list): computer's hand
        water_cards_pile (list): water cards pile
        power_cards_pile (list): power cards pile
        opponent_tank (int): human's water tank level
    Returns:
        2-tuple: (1) computer's water tank level, (2) human's water tank level
    """
    # show the human player's water level and then computer player's
    print(f"Computer's water level is at: {computer_tank}")
    print(f"Your water level is at: {opponent_tank}")

    # calculate lack of players
    computer_lack = 75 - computer_tank
    human_lack = 75 - opponent_tank

    is_discard = False

    # if human lack <= 10, select a card based on human water tank level
    if human_lack <= 10:
        if "DOT" in computer_cards:
            selected_card = "DOT"
        elif "SOH" in computer_cards:
            selected_card = "SOH"
        else:
            selected_card = max(computer_cards[:3])
    # otherwise, select a card based on computer water tank level
    else:
        # if computer has only 1 value water cards, discard one
        if sum(computer_cards[:3]) == 3:
            selected_card = 1
            is_discard = True
        # otherwise, select a card
        elif computer_lack == 75:
            selected_card = max(computer_cards[:3])
        elif 38 <= computer_lack < 75:
            selected_card = "DMT" if "DMT" in computer_cards else max(computer_cards[:3])
        elif 1 < computer_lack < 38:
            selected_card = max(computer_cards[:3])
        else:  # computer_lack == 1
            selected_card = min(computer_cards[:3])

    # take action with the selected card
    if is_discard:
        print(f"Computer discarding card: {selected_card}")
        discard_card(selected_card, computer_cards, water_cards_pile, power_cards_pile)
        computer_tank_update, human_tank_update = computer_tank, opponent_tank
    else:
        print(f"Computer playing with card: {selected_card}")
        computer_tank_update, human_tank_update = use_card(computer_tank, selected_card, computer_cards, opponent_tank)

    # handle overflows
    computer_tank_update = apply_overflow(computer_tank_update)

    # draw a new card of the same type they just used / discarded
    if type(selected_card) == int:
        new = get_card_from_pile(water_cards_pile, 0)
    else:  # type(card) == str
        new = get_card_from_pile(power_cards_pile, 0)

    computer_cards.append(new)
    # keep human's hand arranged after adding the new card
    arrange_cards(computer_cards)

    # print the new tank value for the player and opponent
    print(f"Computer's water level is now at: {computer_tank_update}")
    print(f"Your water level is now at: {human_tank_update}")

    # computer's turn: don't print their hand and the new card they draw
    result = (computer_tank_update, human_tank_update)
    return result


def main():
    # TODO: Write your code as described in the instructions
    # print game instructions
    instructions = """
    Welcome to the WATER TANK game and play against the computer!
    The first player to fill their tank wins the game.
    Good luck!
    """
    print(instructions)

    # set water and power cards pile
    water_cards_pile, power_cards_pile = setup_cards()

    # deal cards and setup human and computer player
    player_1_cards, player_2_cards = deal_cards(water_cards_pile, power_cards_pile)

    human = {
        "name": "Human",
        "cards": player_1_cards,
        "tank": 0,
    }
    computer = {
        "name": "Computer",
        "cards": player_2_cards,
        "tank": 0,
    }

    # choose a random player to go first
    rand_num = randint(0, 1)

    # if random int is 0, human is the first player
    if rand_num == 0:
        player, opponent = human, computer
        is_human_turn = True
    else:
        player, opponent = computer, human
        is_human_turn = False

    print(f"\nThe {player['name']} Player has been selected to go first.")

    # take turns until one player wins
    while True:
        # print whose turn it is
        print(f"\n\n=== {player['name']}'s turn ===")

        # make player's move
        if is_human_turn:
            player["tank"], opponent["tank"] = human_play(player["tank"], player["cards"], water_cards_pile, power_cards_pile, opponent["tank"])
        else:
            player["tank"], opponent["tank"] = computer_play(player["tank"], player["cards"], water_cards_pile, power_cards_pile, opponent["tank"])

        # check if player's tank is filled (wins)
        if filled_tank(player["tank"]):
            print("\n\n === Game Over ===")
            print(f"{player['name']} Player won")
            break

        # check if the cards piles are empty
        check_pile(water_cards_pile, "water")
        check_pile(power_cards_pile, "power")

        # switch turn
        is_human_turn = not is_human_turn
        player, opponent = opponent, player


if __name__ == '__main__':
    main()
