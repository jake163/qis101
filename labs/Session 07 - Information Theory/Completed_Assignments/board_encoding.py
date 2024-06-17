#!/usr/bin/env python3
# board_encoding.py
import numpy as np

# This is where I found out how to print a tic tac toe board:
# https://stackoverflow.com/questions/44269612/python-drawing-a-tic-tac-toe-board


def decode_trinary(number: int) -> list:
    board = [0] * 9  # initialize empty board
    counter = 0
    while (
        number / 3 >= 1
    ):  # for a number n, find n mod 3 = x, add x to list, then n' = n/3.
        # rinse and repeat
        board[counter] = number % 3
        number = number // 3
        counter += 1
    while number / 3 < 1:  # for the last x, n is less than three
        board[counter] = number
        break  # we need to break after one iteration
    return board


def draw_board(board: list) -> str:
    for j, number in enumerate(board):  # substitute numbers for characters
        if number == 1:
            board[j] = "X"
        if number == 2:
            board[j] = "O"
        if number == 0:
            board[j] = " "
    c_board = board  # "character board"
    pc_board = ""  # "printable character board"
    for i in range(0, 9, 3):  # print board for each number
        pc_board += f"  {c_board[i]}  |  {c_board[i+1]}  |  {c_board[i+2]}   \n"
        if i <= 3:
            pc_board += " ---- " * 3
            pc_board += "\n"
    return pc_board


def main():  # executable from command line
    for i in range(3):
        numbers = [2271, 1638, 12065]
        number = numbers[i]
        drawn_board = draw_board(
            decode_trinary(number)
        )  # pass number into decode_trinary(),
        # which is then passed into draw_board
        print(f"The number {number} encodes the board: \n \n{drawn_board}")


if __name__ == "__main__":
    main()
