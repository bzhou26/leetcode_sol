'''
- Leetcode problem: 348

- Difficulty: Medium

- Brief problem description:

Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?

- Solution Summary:

O(n**2) solution, it can be improved

- Used Resources:

--- Bo Zhou
'''


class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.win = 0
        self.size = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """

        if self.win > 0:
            return self.win

        self.board[row][col] = player

        n = self.size
        for i in range(n):
            hMove = 0
            for j in range(n):
                if self.board[i][j] > 0 and hMove == 0:
                    hMove = self.board[i][j]
                elif self.board[i][j] == 0 or self.board[i][j] != hMove:
                    break
                elif j == n - 1 and self.board[i][j] == hMove:
                    self.win = hMove

        for j in range(n):
            hMove = 0
            for i in range(n):
                if self.board[i][j] > 0 and hMove == 0:
                    hMove = self.board[i][j]
                elif self.board[i][j] == 0 or self.board[i][j] != hMove:
                    break
                elif i == n - 1 and self.board[i][j] == hMove:
                    self.win = hMove

        hMove = 0
        for i in range(n):
            if self.board[i][i] > 0 and hMove == 0:
                hMove = self.board[i][i]
            elif self.board[i][i] == 0 or self.board[i][i] != hMove:
                break
            elif i == n - 1 and self.board[i][i] == hMove:
                self.win = hMove

        hMove = 0
        for i in range(n):
            if self.board[i][n - 1 - i] > 0 and hMove == 0:
                hMove = self.board[i][n - 1 - i]
            elif self.board[i][n - 1 - i] == 0 or self.board[i][n - 1 - i] != hMove:
                break
            elif i == n - 1 and self.board[i][n - 1 - i] == hMove:
                self.win = hMove

        return self.win

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)