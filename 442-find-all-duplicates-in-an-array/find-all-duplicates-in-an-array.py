class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[]
        kick=set()
        for num in nums:
            if num  in kick:
                arr.append(num)
            kick.add(num)
        return arr
        