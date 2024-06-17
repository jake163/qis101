#!/usr/bin/env python3
# dealer_bogus.py

import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = [
    "Deuce",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
]


def init_deck():  # gives us an ordered card deck
    return list(range(52))  # return list such that each index number is the value at
    # that index: 0 and index 0, 1 at index 1, etc. Do it by plugging a range
    # (0 to 51) into the list function


def card_name(card_num):
    name = f"{ranks[card_num % 13]} of {suits[card_num // 13]}"
    return name


def display_deck(deck):
    for card_pos, card_num in enumerate(deck):
        print(f"The card in position {card_pos} is the {card_name(card_num)}")
<<<<<<< HEAD
        # print(f"The card in position {card_pos} is the {card_num}")
=======
>>>>>>> 8714fac53a740147291686210ad82b687caf566b


def deal_cards(deck):  # function to shuffle cards, pass in the ordered deck
    for card_pos, _ in enumerate(deck):  # unpack tuples (card_pos, "") in deck []
        new_card_num = random.randint(0, 51)  # randomly give us a valid card number
        deck[card_pos] = new_card_num  # for each card_pos (index), we assign a random
        # card number. Problem is we can have repeat numbers, and each card in a deck
        # (the card number) is supposed to be unique.


def main():
    random.seed(2016)  # imported random number generator, initial value of 2016,
    # help us shuffle
    deck = init_deck()  # initialize our deck
    deal_cards(deck)  # take our ordered deck, and pass into deal_cards() which should
    # shuffle those cards
    display_deck(deck)


if __name__ == "__main__":
    main()
