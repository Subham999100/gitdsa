class Solution(object):
    def reverseString(self, s):
        def recur(left,right):
            if left>=right:
                return
                
            s[left],s[right]=s[right],s[left]
            recur(left+1,right-1)
        recur(0,len(s)-1)
            
        