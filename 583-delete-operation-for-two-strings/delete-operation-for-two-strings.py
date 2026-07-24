class Solution(object):
    def solve(self,s1,s2,i,j,dp):
        if i==len(s1):
            return len(s2)-j
        if j==len(s2):
            return len(s1)-i
        if dp[i][j]!=-1:
            return dp[i][j]
        if s1[i]==s2[j]:
            dp[i][j]=self.solve(s1,s2,i+1,j+1,dp)
        else:
            dp[i][j]=1+min(self.solve(s1,s2,i+1,j,dp),self.solve(s1,s2,i,j+1,dp))
        return dp[i][j]
        
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n=len(word1)
        m=len(word2)
        dp=[[-1]*m for _ in range(n)]
        return self.solve(word1,word2,0,0,dp)
        