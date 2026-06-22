class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi=max(nums)
        ans=0
        while k!=0:
            ans+=maxi
            maxi+=1
            k-=1
        return ans
