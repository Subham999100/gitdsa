class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum=0
        i=j=0
        avg=0
        maxavg=float('-inf')
        while(j<len(nums)):
            sum+=nums[j]
            if(j-i+1<k):
                j+=1
            elif(j-i+1==k):
                avg=sum/float(k)
                maxavg=max(maxavg,avg)
                sum-=nums[i]
                i+=1
                j+=1
        return maxavg
        

        