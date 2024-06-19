#!/usr/bin/env python3
# dealer_slow.py

import random
import time


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


def init_deck():
    return list(range(52))


def card_name(card_num):
    name = f"{ranks[card_num % 13]} of {suits[card_num // 13]}"
    return name


def display_deck(deck):
    for card_pos, card_num in enumerate(deck):
        print(f"The card in position {card_pos} is the {card_name(card_num)}")


<<<<<<< HEAD
def deal_cards(deck):
    already_dealt = [False] * 52
    for card_pos, _ in enumerate(deck):
        new_card_num = random.randint(0, 51)
        while already_dealt[new_card_num]:
            new_card_num = random.randint(0, 51)
        deck[card_pos] = new_card_num
        already_dealt[new_card_num] = True


def main():
    random.seed(2016)

    deck = init_deck()

    total_deals = 10000

    start_time = time.process_time()

    for _ in range(0, total_deals):
        deal_cards(deck)

    elapsed_time = time.process_time() - start_time

    display_deck(deck)

    print(f"Total deals: {total_deals:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")
=======
def deal_cards(deck):  # pass in the ordered deck to be shuffled
    already_dealt = [False] * 52  # list of "false" bools, 52 of them
    for card_pos, _ in enumerate(deck):  # iterate through list of tuples (deck)
        new_card_num = random.randint(0, 51)  # randomly pick new valid card number
        while already_dealt[new_card_num]:  # if card has already been dealt
            new_card_num = random.randint(0, 51)  # pick another random number
        deck[card_pos] = new_card_num  # deck index is assigned the value new_card_num
        already_dealt[new_card_num] = True  # This keeps track of what card_num has been
        # used. If a used card_num gets drawn again, then already_dealt[]=true, and
        # another card is draw until already_dealt[]=false

        # however this is inefficient, as we get to the end of the deck, it will take
        # longer and longer to randomly pick a card_num that hasn't already been picked


def main():
    random.seed(2016)  # r imported andom number generator, initial value of 2016

    deck = init_deck()  # function creates our deck

    total_deals = 10000  # assign int 10000 to variable "total_deals"

    start_time = time.process_time()  # the time module measures cpu time

    for _ in range(0, total_deals):  # run card shuffle function 10000 times, time
        # this process
        deal_cards(deck)

    elapsed_time = time.process_time() - start_time  # figure out how much time has
    # passed

    display_deck(deck)  # show the cards and their position in the deck of the last
    # shuffle

    print(f"Total deals: {total_deals:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")  # prints time to deal
    # 10000 decks to three digits, \n creates a new blank line that follows {}
>>>>>>> 09efffcfbb028c8b77c33772285a978b2c071a9a


if __name__ == "__main__":
    main()
