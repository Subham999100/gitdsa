class Solution(object):
    def findcomb(self,i,c,t,ls,ds):
        if(i==len(c)):
            if(t==0):
                ls.append(list(ds))
            return
        if(c[i]<=t):
            ds.append(c[i])
            self.findcomb(i,c,t-c[i],ls,ds)
            ds.pop()
        self.findcomb(i+1,c,t,ls,ds)
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        arr=[]
        ds=[]
        self.findcomb(0,candidates,target,arr,ds)
        return arr

        