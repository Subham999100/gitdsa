class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=""
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for ch,count in sorted(freq.items(),key=lambda x:x[1],reverse=True):
            ans+=ch*count
        return ans


        