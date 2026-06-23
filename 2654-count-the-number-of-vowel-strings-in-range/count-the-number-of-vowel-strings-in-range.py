class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        vow="aeiou"
        ans=0
        for i in range(left,right+1):
            if(words[i][0]  in vow and words[i][-1] in vow):
                ans+=1
        return ans


        