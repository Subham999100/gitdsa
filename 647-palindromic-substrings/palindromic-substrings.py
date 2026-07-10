class Solution(object):
    def solve(self,s,i,j,dp):
        if(i>=j):
            return True
        if(dp[i][j]!=-1):
            return dp[i][j]
        if(s[i]==s[j]):
            dp[i][j]=self.solve(s,i+1,j-1,dp)
        else:
            dp[i][j]=False
        return dp[i][j]

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        count=0
        dp=[[-1]*n for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                if(self.solve(s,i,j,dp)==True):
                    count+=1
        return count

        