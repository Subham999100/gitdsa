class Solution(object):
    def threeSum(self, n):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n.sort()
        res=[]
        for i in range(len(n)-2):
            if( i>0 and n[i]==n[i-1]):
                continue
            lf=i+1
            rg=len(n)-1
            while(lf<rg):
                s=n[lf]+n[rg]
                tar=-n[i]
                if(s==tar):
                    res.append([n[i],n[lf],n[rg]])
                    lf+=1
                    rg-=1
                    while(lf<rg and n[lf]==n[lf-1]):
                        lf+=1
                    while(lf<rg and n[rg]==n[rg+1]):
                        rg-=1
                elif(s<tar):
                    lf+=1
                else:
                    rg-=1
        return res
                

