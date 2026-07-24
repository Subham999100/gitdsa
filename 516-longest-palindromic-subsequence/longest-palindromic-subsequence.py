class Solution(object):
    def solve(self,s1,s2,i,j,dp):
        if((i>=len(s1)) or(j>=len(s2))):
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        if(s1[i]==s2[j]):
            dp[i][j]=1+self.solve(s1,s2,i+1,j+1,dp)
        else:
            dp[i][j]=max(self.solve(s1,s2,i+1,j,dp),self.solve(s1,s2,i,j+1,dp))
        return dp[i][j]
    def longestPalindromeSubseq(self, s):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        text1=s
        text2=s[::-1]
        dp=[[-1]*len(text2) for _ in range(len(text1))]
        return self.solve(text1,text2,0,0,dp)
                