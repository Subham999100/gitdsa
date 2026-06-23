class Solution(object):
    def isvow(self,s):
        kk="aeiou"
        if s[0] in kk and s[-1] in kk:
            return True
        return False
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        ans=0
        for i in range(left,right+1):
            if(self.isvow(words[i])):
                ans+=1
        return ans


        