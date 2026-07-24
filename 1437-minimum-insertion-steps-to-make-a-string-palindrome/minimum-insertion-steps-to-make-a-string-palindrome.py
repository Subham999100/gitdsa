class Solution(object):
    def solve(self,s,i,j,dp):
        if(i>=j):
            return 0
        if(dp[i][j]!=-1):
            return dp[i][j]
        if(s[i]==s[j]):
            dp[i][j]=self.solve(s,i+1,j-1,dp)
        else:
            dp[i][j]=1+min(self.solve(s,i+1,j,dp),self.solve(s,i,j-1,dp))
        return dp[i][j]
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[[-1]*n for _ in range(n)]
        return self.solve(s,0,n-1,dp)