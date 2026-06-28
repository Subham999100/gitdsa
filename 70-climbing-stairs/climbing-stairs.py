class Solution(object):
    def solve(self,i,n,dp):
        if i==n:
            return 1
        if i>n:
            return 0
        if dp[i]!=-1:
            return dp[i]
        one=self.solve(i+1,n,dp)
        two=self.solve(i+2,n,dp)
        dp[i]= one+two
        return dp[i]
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1]*(n+1)
        return self.solve(0,n,dp)

        