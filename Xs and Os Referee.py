#this is my solution of Chekio mission Xs and Os Referee (https://py.checkio.org/en/mission/x-o-referee/)

"""Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the spaces
in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows
(NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results. You are given a result of a game
and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to return "X"
if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D"."""

from typing import List

def checkio(game_result: List[str]) -> str:
    for row in game_result:
        if row[0] == row[1] == row[2] and row[0] != '.':
            return row[0]

    for i in range(3):
        if game_result[0][i] == game_result[1][i] == game_result[2][i] and game_result[0][i] != '.':
            return game_result[0][i]

    if game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[0][0] != '.':
        return game_result[0][0]
    if game_result[2][0] == game_result[1][1] == game_result[0][2] and game_result[2][0] != '.':
        return game_result[2][0]

    return "D"

# These tests was created by Chekio.

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
