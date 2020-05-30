'''
- Leetcode problem: 322

- Difficulty: Medium

- Brief problem description:

You are given coins of different denominations and a total amount of money amount. Write a function to compute the
fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

- Solution Summary:

Typical DP solution, for example, coins are [1, 2, 5], amount = 11
F(1) = -1
F(2) = -1
.
.
.
F(6) = min (F(6-1)+1, F(6-2)+1, F(6-5)+1)
.
.
.
F(11) = min (F(11-1)+1, F(11-2)+1, F(11-5)+1)
NOTE: Only calculate when F(n) != -1 because -1 means not possible.

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def coinChange(self, coins, amount) -> int:
        minCoins = [0]
        i = 1
        while i <= amount:
            minCoin = -1
            for c in coins:
                if i - c >= 0:
                    if minCoins[i - c] == -1:
                        continue
                    if minCoin != -1:
                        minCoin = min(minCoins[i - c] + 1, minCoin)
                    else:
                        minCoin = minCoins[i - c] + 1
            minCoins.append(minCoin)
            i += 1
        return minCoins[amount]


if __name__ == "__main__":
    solution = Solution()
    testList = [186,419,83,408]
    print(solution.coinChange(testList, 6249))