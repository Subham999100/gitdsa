class Solution(object):
    def twoSum(self, nums, target):
        di={}
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in di:
                return [di[comp],i]
            di[nums[i]]=i
            
        