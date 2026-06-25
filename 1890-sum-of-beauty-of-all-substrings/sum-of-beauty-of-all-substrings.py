class Solution(object):
    def beautySum(self, s):
        n=len(s)
        ans=0
        for i in range(n):
            f={}
            for j in range(i,n):
                c=s[j]
                f[c]=f.get(c,0)+1
                ans+=max(f.values())-min(f.values())
        return ans