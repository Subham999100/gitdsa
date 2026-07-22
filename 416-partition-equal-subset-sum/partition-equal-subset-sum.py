class Solution(object):
    def solve(self,i,nums,x,dp):
        if(x==0):
            return True
        if(i>=len(nums)):
            return False
        if dp[i][x]!=-1:
            return dp[i][x]
        add=False
        if(x>=nums[i]):
            add=self.solve(i+1,nums,x-nums[i],dp)
        minu=self.solve(i+1,nums,x,dp)
        dp[i][x]=add or minu
        return dp[i][x]
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sumi=sum(nums)
        n=len(nums)
        x=sumi/2
        dp=[[-1]*(x+1) for _ in range(n)]
        if(sumi%2!=0):
            return False
        return self.solve(0,nums,x,dp)