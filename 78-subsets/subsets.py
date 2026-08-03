class Solution(object):
    def solve(self,res,cur,nums,i):
        if(i>=len(nums)):
            res.append(cur[:])
            return
        cur.append(nums[i])
        self.solve(res,cur,nums,i+1)
        cur.pop()
        self.solve(res,cur,nums,i+1)
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        cur=[]
        self.solve(res,cur,nums,0)
        return res