class Solution(object):
    def solve(self,cand,tar,res,i,cur):
        if(tar<0):
            return 
        if(tar==0):
            res.append(cur[:])
            return
        for j in range(i,len(cand)):
            if(j>i and cand[j]==cand[j-1]):
                continue
            cur.append(cand[j])
            self.solve(cand,tar-cand[j],res,j+1,cur)
            cur.pop()

    def combinationSum2(self, candidates, target):
        res=[]
        cur=[]
        candidates.sort()
        self.solve(candidates,target,res,0,cur)
        return res
        