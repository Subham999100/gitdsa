class Solution(object):
    def solve(self,s,i,j,dp):
        if i>=j:
            return True
        if dp[i][j]!=-1:
            return dp[i][j]
        if(s[i]==s[j]):
            dp[i][j]=self.solve(s,i+1,j-1,dp)
        else:
            dp[i][j]=False
        return dp[i][j]
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        maxlen=0
        sp=0
        dp=[[-1]* n for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                if(self.solve(s,i,j,dp)==True):
                    if(j-i+1>maxlen):
                        maxlen=j-i+1
                        sp=i
        return s[sp:sp+maxlen]
        