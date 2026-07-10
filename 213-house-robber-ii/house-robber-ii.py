class Solution(object):
    def solve(self,i,arr,n,dp):
        if(i>n):
            return 0
        if dp[i]!=-1:
            return dp[i]
        sumi=arr[i]+self.solve(i+2,arr,n,dp)
        sumk=self.solve(i+1,arr,n,dp)
        dp[i]=max(sumi,sumk)
        return dp[i]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        n=len(nums)
        dp1=[-1]*(n)
        ans1=self.solve(0,nums,n-2,dp1)
        dp2=[-1]*(n)
        ans2=self.solve(1,nums,n-1,dp2  )
        return max(ans1,ans2)
        