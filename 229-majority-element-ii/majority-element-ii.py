class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        high=len(nums)/3
        freq={}
        arr=[]
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
            if freq[num]>high:
                if num not in arr:
                    arr.append(num)
        return arr
            