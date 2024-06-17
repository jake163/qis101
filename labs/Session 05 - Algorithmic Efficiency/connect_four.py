#!/usr/bin/env python3
# connect_four.py


def is_winner(board: list) -> str:  # pass in boards, returns a corresponding string
    counter = 0
    for i, array in enumerate(board):  # iterate through list of lists
        for j, num in enumerate(array):  # iterate through each list
            for k in range(1, 3):  # piece 1 or 2, red or black
                if int(num) == k:  # if a piece on the board is red or black
                    i = int(i)
                    j = int(j)
                    if i <= 2 and j <= 6:  # specify regions inside the board
                        if board[i + 1][j] == k:  # is there a vertical connect four?
                            if board[i + 2][j] == k:
                                if board[i + 3][j] == k:
                                    counter += k  # add piece number to counter
                    if i <= 5 and j <= 3:
                        if board[i][j + 1] == k:  # is there a horizontal connect four?
                            if board[i][j + 2] == k:
                                if board[i][j + 3] == k:
                                    counter += k
                    if i <= 2 and j <= 3:
                        if (
                            board[i + 1][j + 1] == k
                        ):  # is there a right-diagonal connect four?
                            if board[i + 2][j + 2] == k:
                                if board[i + 3][j + 3] == k:
                                    counter += k
                    if i <= 2 and j >= 3:
                        if (
                            board[i + 1][j - 1] == k
                        ):  # is there a left-diagonal connect four?
                            if board[i + 2][j - 2] == k:
                                if board[i + 3][j - 3] == k:
                                    counter += k
    if counter == 1:
        winner = "Player 1"  # player one is 1 or red
    if counter == 2:
        winner = "Player 2"  # player two is 2 or back
    if counter == 0:
        winner = "Nobody"
    return winner


def main():
    board1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]

    board2 = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]

    board3 = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]

    boards = [board1, board2, board3]

    for num, board in enumerate(boards):
        print(f"{is_winner(board)} is the winner of board {num+1}")


if __name__ == "__main__":
    main()
