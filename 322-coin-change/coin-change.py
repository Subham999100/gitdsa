class Solution(object):

    def solve(self, i, amount, coins, dp):

        if amount == 0:
            return 0

        if amount < 0:
            return float('inf')

        if i == len(coins):
            return float('inf')

        if dp[i][amount] != -1:
            return dp[i][amount]

        take = 1 + self.solve(i, amount - coins[i], coins, dp)

        skip = self.solve(i + 1, amount, coins, dp)

        dp[i][amount] = min(take, skip)

        return dp[i][amount]

    def coinChange(self, coins, amount):

        n = len(coins)

        dp = [[-1]*(amount+1) for _ in range(n)]

        ans = self.solve(0, amount, coins, dp)

        if ans == float('inf'):
            return -1

        return ans