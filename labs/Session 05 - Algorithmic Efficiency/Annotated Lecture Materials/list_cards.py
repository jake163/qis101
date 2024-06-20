#!/usr/bin/env python3
# list_cards.py


suits = ["Clubs", "Diamonds", "Hearts", "Spades"]  # list of suits of cards as strings,
# global variable
ranks = [  # horizontally list card numbers (ranks) as strings, global variable
    "Deuce",  # "2" card is the zero index of this list, it is a string
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


def init_deck():  # create a deck of cards as a list of card numbers
    deck = [None] * 52  # create a list with 52 empty slots
    for card_pos, _ in enumerate(deck):  # iterating through empty list,
        # unpack tuple of card position variable and _ ->
        # [(0, ''), (1, ''), ...]
        deck[card_pos] = card_pos  # assign each card number to its position
    return deck  # return labelled deck list


def card_name(card_num):
    name = f"{ranks[card_num % 13]} of {suits[card_num // 13]}"  # for each card number,
    # we get a unique string. We control the placeholders (rank and suit) by inputting
    # the index of the list where rank and suit of the unique card are found
    return name


def display_deck(deck):
    for card_pos, card_num in enumerate(deck):  # unpack tuple in deck, indices still
        # labelled as card_pos, but now the values are card_num
        print(f"The card in position {card_pos} is the {card_name(card_num)}")


def main():  # function executable from command line, calls init_deck()
    deck = init_deck()
    display_deck(deck)


if __name__ == "__main__":
    main()
