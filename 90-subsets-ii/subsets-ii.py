class Solution(object):
    def solve(self,res,cur,nums,idx):
        if(idx>=len(nums)):
            res.append(cur[:])
            return
        cur.append(nums[idx])
        self.solve(res,cur,nums,idx+1)
        cur.pop()
        while(idx+1<len(nums) and nums[idx]==nums[idx+1]):
            idx+=1
        self.solve(res,cur,nums,idx+1)
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        cur=[]
        nums.sort()
        self.solve(res,cur,nums,0)
        return res
        