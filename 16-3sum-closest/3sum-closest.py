class Solution(object):
    def threeSumClosest(self, n, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n.sort()
        mini=float('inf')
        best=0
        for i in range(len(n)-2):
            if(i>0 and n[i]==n[i-1]):
                continue
            lf=i+1
            rg=len(n)-1
            while(lf<rg):
                s=n[lf]+n[rg]+n[i]
                if(mini>abs(s-target)):
                    best=s
                    mini=abs(s-target)
                if(s>target):
                    rg-=1
                else:
                    lf+=1
        return best



        