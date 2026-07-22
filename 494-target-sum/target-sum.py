class Solution(object):
    def solve(self,sumi,nums,i,cursum,target,dp):
        if(i==len(nums)):
            if(cursum==target):
                return 1
            else:
                return 0
        if dp[i][cursum+sumi]!=-1:
            return dp[i][cursum+sumi]
        plus=self.solve(sumi,nums,i+1,cursum+nums[i],target,dp)
        minu=self.solve(sumi,nums,i+1,cursum-nums[i],target,dp)
        dp[i][cursum+sumi]=plus+minu
        return dp[i][cursum+sumi]
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sumi=sum(nums)
        n=len(nums)
        dp=[[-1]*(2*sumi+1) for _ in range (n)]
        return self.solve(sumi,nums,0,0,target,dp)
        