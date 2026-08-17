class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        kick={}
        for i in range(len(nums)):
            kick[nums[i]]=kick.get(nums[i],0)+1
        for key,val in kick.items():
            if val==1:
                sum+=key
        return sum
        