'''
- Leetcode problem: 79

- Difficulty: Medium

- Brief problem description:

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or
vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    result |= self.dfs(word, 0, i, j, board, set())
                    if result:
                        return True
        return False

    def dfs(self, word, n, x, y, board, visited):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or (x, y) in visited:
            return False
        if n == len(word) - 1:
            if word[n] == board[x][y]:
                return True
            else:
                return False
        if word[n] != board[x][y]:
            return False
        result = False
        visited.add((x, y))
        result |= self.dfs(word, n + 1, x + 1, y, board, visited)
        if not result:
            result |= self.dfs(word, n + 1, x - 1, y, board, visited)
        if not result:
            result |= self.dfs(word, n + 1, x, y + 1, board, visited)
        if not result:
            result |= self.dfs(word, n + 1, x, y - 1, board, visited)
        visited.remove((x, y))
        return result
