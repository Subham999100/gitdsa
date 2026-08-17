class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum=0
        count=0
        kick={}
        kick[0]=1
        for i in range(len(nums)):
            sum+=nums[i]
            comp=sum-k
            if(comp in kick):
                count+=kick[comp]
            kick[sum]=kick.get(sum,0)+1

        return count
        
        