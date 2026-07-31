class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        kick=set()
        i=0
        ans=0
        for j in range(len(s)):
            while s[j] in kick:
                kick.remove(s[i])
                i+=1
            kick.add(s[j])
            ans=max(ans,j-i+1)
        return ans 

        