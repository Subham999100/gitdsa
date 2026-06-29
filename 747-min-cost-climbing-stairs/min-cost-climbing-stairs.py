class Solution(object):
        def solve(self,i,n,dp,c):
            if i>=n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            one=c[i]+ self.solve(i+1,n,dp,c)
            two=c[i]+ self.solve(i+2,n,dp,c)
            dp[i]=min(one,two)
            return dp[i]
            
            
        def minCostClimbingStairs(self, c):
            """
            :type cost: List[int]
            :rtype: int
            """
            n=len(c)
            dp=[-1]*(len(c)+1)
            return min(
                self.solve(0,n,dp,c),
                self.solve(1,n,dp,c)
            )
            