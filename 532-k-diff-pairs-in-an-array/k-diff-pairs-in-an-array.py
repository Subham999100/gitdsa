class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i=0
        j=1
        ans=0
        while j<len(nums):
            if i==j:
                j+=1
                continue
            kk=nums[j]-nums[i]
            if(kk==k):
                ans+=1
                i+=1
                j+=1
                while j<len(nums) and nums[j]==nums[j-1]:
                    j+=1
            elif kk<k:
                j+=1
            else:
                i+=1
        return ans
