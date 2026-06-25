class Solution(object):
    def beautifulSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res=0
        vowe="aeiou"
        for i in range(len(s)):
            vow=0
            con=0
            for j in range(i,len(s)):
                if(s[j] in vowe):
                    vow+=1
                else:
                    con+=1
                if(vow==con and (vow*con)%k==0):
                    res+=1
        return res