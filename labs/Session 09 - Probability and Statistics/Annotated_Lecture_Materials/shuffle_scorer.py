#!/usr/bin/env python3
# shuffle_scorer.py

import numpy as np
import random


def deal_cards(deck):  # number cards
    hands = np.zeros((4, 4, 13), dtype=int)  # four by four by thirteen array of zeros
    for card_pos, card_num in enumerate(deck):
        hand_num = card_pos % 4  # how to numerically represent hands
        suit_num = card_num // 13
        rank_num = card_num % 13
        hands[hand_num][suit_num][
            rank_num
        ] = 1  # the indices represent number, suit, rank,
        # while the 1 says there is one card with those parameters
    return hands


def score_deal(hands):
    score = 0
    for player in range(4):
        # Ideally each player would have 3.25 cards of each suit
        for suit in range(4):
            score += (
                np.sum(hands[player][suit]) - 3.25
            ) ** 2  # the lower this is, the better

        # Ideally each player would have one card of each rank
        for rank in range(13):
            score += (hands[player][0][rank] - 1) ** 2
            score += (hands[player][1][rank] - 1) ** 2
            score += (hands[player][2][rank] - 1) ** 2
            score += (hands[player][3][rank] - 1) ** 2

    return score


def wash_shuffle(deck):  # implements wash shuffle when we pass in the deck
    for card_pos, card_num in enumerate(deck):  # iterate through tuples in deck
        new_card_pos = random.randint(0, 51)  # rearrange (swap) cards in new positions
        deck[card_pos] = deck[new_card_pos]
        deck[new_card_pos] = card_num
    return deck


def riffle_shuffle(deck):  # pass in deck to pull of a riffle shuffle
    # Cut the deck into two equal halves
    left_pile = deck[:26]
    right_pile = deck[26:]
    # Prepare a new empty deck to hold the riffled halves
    new_deck = np.zeros(0, dtype=int)
    while len(new_deck) < 52:
        # Riffle in a set of cards from the left pile
        chunk = random.randint(1, 4)  # random number from 1 to 3
        new_deck = np.append(new_deck, left_pile[:chunk])  # take a chunk of cards
        # from left pile, randomize the index, put into new pile
        left_pile = left_pile[chunk:]  # whatever remains after we take out a chunk
        # Riffle in a set of cards from the right pile
        chunk = random.randint(1, 4)
        new_deck = np.append(new_deck, right_pile[:chunk])
        right_pile = right_pile[chunk:]
    return new_deck


def score_shuffle(shuffle_func, num_deals=10_000):  # pass in shuffle_func(), num_deals
    total_score = 0
    deck = np.arange(52, dtype=int)  # 52 unique cards
    for _ in range(num_deals):  # iterate 10,000 times
        deck = shuffle_func(deck)  # deck is shuffled
        total_score += score_deal(deal_cards(deck))  # evaluate randomness of shuffle
    return total_score / num_deals  # average random score across decks


def main():
    random.seed(2016)
    print(f"Wash Shuffle Avg. Score = {score_shuffle(wash_shuffle)}")  # print function
    # with an inputted function, evaluates result of wash_shuffle
    print(f"Riffle Shuffle Avg. Score = {score_shuffle(riffle_shuffle)}")


if __name__ == "__main__":
    main()
