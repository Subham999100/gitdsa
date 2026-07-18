class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=min(nums)
        l=max(nums)

        while(l!=0):
            s,l=l,s%l
        return s
        
