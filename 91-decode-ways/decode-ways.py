class Solution(object):
    def solve(self,i,s,n,dp):
        if i==n:
            return 1
        if dp[i]!=-1:
            return dp[i]
        if s[i]=='0':
            return 0
        res=self.solve(i+1,s,n,dp)
        if(i+1<n):
            if((s[i]=='1') or (s[i]=='2' and s[i+1]<='6')):
                res+=self.solve(i+2,s,n,dp)
        dp[i]=res
        return dp[i]
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[-1]*(n)
        return self.solve(0,s,n,dp)
        