class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def solve(start,end):
            if(start>=end):
               return
            temp=s[start]
            s[start]=s[end]
            s[end]=temp
            return solve(start+1,end-1)
        return solve(0,len(s)-1)