class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp={}
        for i in range(len(numbers)):
            diff=target-numbers[i]
            if diff in mp:
                return [mp[diff]+1,i+1]
            
            mp[numbers[i]]=i
        