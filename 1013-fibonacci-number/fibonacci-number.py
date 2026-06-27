class Solution(object):
    def solve(self,dp,n):
        if n<=1:
            return n
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.solve(dp,n-1)+self.solve(dp,n-2)
        return dp[n]
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return n
        dp=[-1]*(n+1)
        return self.solve(dp,n)
        