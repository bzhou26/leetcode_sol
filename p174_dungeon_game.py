class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        state = [[999999999999 for i in range(n + 1)] for j in range(m + 1)]
        state[m][n-1] = 1
        state[m-1][n] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                need = min(state[i][j + 1], state[i + 1][j]) - dungeon[i][j]
                if need <= 0:
                    state[i][j] = 1
                else:
                    state[i][j] = need
        return state[0][0]
        