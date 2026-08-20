class Solution(object):
    def numRescueBoats(self, p, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        p.sort()
        i=0
        j=len(p)-1
        b=0
        while(i<=j):
            if(p[i]+p[j]<=limit):
                b+=1
                i+=1
                j-=1
            elif(p[i]+p[j]>limit):
                b+=1
                j-=1
        return b




        