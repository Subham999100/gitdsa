class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq={}
        if len(s)!=len(t):
            return False
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for kh in t:
            freq[kh]=freq.get(kh,0)-1
        for kk in freq.values():
            if kk>0:
                return False
        return True
        