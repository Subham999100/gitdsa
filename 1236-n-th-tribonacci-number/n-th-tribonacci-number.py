class Solution(object):
    
    def solve(self,n,dp):
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        if dp[n]!=-1:
            return dp[n
            ]
        dp[n]=self.solve(n-3,dp)+ self.solve(n-2,dp)+self.solve(n-1,dp)
        return dp[n]

    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1]*(n+1)
        return self.solve(n,dp)
        