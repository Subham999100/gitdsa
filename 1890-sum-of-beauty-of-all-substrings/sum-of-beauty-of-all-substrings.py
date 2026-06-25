class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        for i in range(len(s)):
            freq=[0]*26
            for j in range(i,len(s)):
                freq[ord(s[j])-ord('a')]+=1
                mx=0
                mn=float("inf")
                for f in  freq:
                    if f>0:
                        mx=max(f,mx)
                        mn=min(f,mn)        
                ans+=mx-mn
        return ans
        