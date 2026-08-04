class Solution(object):
    def ispali(self,s,l,r):
        while(l<r):
            if(s[l]!=s[r]):
                return False
            l+=1
            r-=1
        return True
    def solve(self,i,s,res,cur,n):
        if(i>=n):
            res.append(cur[:])
            return
        for j in range(i,n):
            if(self.ispali(s,i,j)):
                cur.append(s[i:j+1])
                self.solve(j+1,s,res,cur,n)
                cur.pop()


    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n=len(s)
        res=[]
        cur=[]
        self.solve(0,s,res,cur,n)
        return res
        