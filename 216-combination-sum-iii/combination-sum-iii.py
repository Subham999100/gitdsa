class Solution(object):
    def solve(self,i,cur,res,k,n):
        if n==0 and len(cur)==k:
            res.append(cur[:])
            return
        if i>9 or n<0 or len(cur)>k:
            return
        cur.append(i)
        self.solve(i+1,cur,res,k,n-i)
        cur.pop()
        self.solve(i+1,cur,res,k,n)    
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res=[]
        cur=[]
        self.solve(1,cur,res,k,n)
        return res
        