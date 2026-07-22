class Solution(object):
    def solve(self, n, dp):
        if n == 0:
            return 0

        if dp[n] != -1:
            return dp[n]

        ans = float('inf')
        i = 1
        while i * i <= n:
            ans = min(ans, 1 + self.solve(n - i * i, dp))
            i += 1

        dp[n] = ans
        return ans

    def numSquares(self, n):
        dp = [-1] * (n + 1)
        return self.solve(n, dp)