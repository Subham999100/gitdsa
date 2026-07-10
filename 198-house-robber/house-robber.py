class Solution(object):
    def solve(self,i,arr,dp):
        if i>=len(arr):
            return 0
        if dp[i]!=-1:
            return dp[i]
        sumi=arr[i]+self.solve(i+2,arr,dp)
        sumk=self.solve(i+1,arr,dp)
        dp[i]=max(sumi,sumk)
        return dp[i]
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[-1]*(n)
        return self.solve(0,nums,dp)
        