'''
- Leetcode problem: 130

- Difficulty: Medium

- Brief problem description:

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to
'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells
are connected if they are adjacent cells connected horizontally or vertically.

- Solution Summary:

1. Find all 'O's on the board
2. Use dfs to mark all 'O's which are connected to the 'O's we found in step 1 ( mark them to 'a')
3. Go though all point again, flip 'O's to 'X' and flip 'a's to 'O'

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2:
            return board

        bZeros = set()
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                bZeros.add((0, i))
            if board[-1][i] == 'O':
                bZeros.add((len(board) - 1, i))
        for j in range(len(board)):
            if board[j][0] == 'O':
                bZeros.add((j, 0))
            if board[j][len(board[0]) - 1] == 'O':
                bZeros.add((j, len(board[0]) - 1))

        for x, y in bZeros:
            self.dfs(board, x, y)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'a':
                    board[i][j] = 'O'

    def dfs(self, board, x, y):
        if x < 0 or x > len(board) - 1 or y < 0 or y > len(board[0]) - 1 or board[x][y] != 'O':
            return
        board[x][y] = 'a'
        self.dfs(board, x + 1, y)
        self.dfs(board, x - 1, y)
        self.dfs(board, x, y + 1)
        self.dfs(board, x, y - 1)
