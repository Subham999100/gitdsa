class Solution(object):
    def solve(self,i,amount,coins,dp):
        if amount==0:
            return 1
        if i>=len(coins):
            return 0
        if dp[i][amount]!=-1:
            return dp[i][amount]
        take=0
        if coins[i]<=amount:
            take=self.solve(i,amount-coins[i],coins,dp)
        nottake=self.solve(i+1,amount,coins,dp)
        dp[i][amount]=take+nottake
        return dp[i][amount]
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n)]
        ans=self.solve(0,amount,coins,dp)
        if ans==float('inf'):
            return 0
        return ans