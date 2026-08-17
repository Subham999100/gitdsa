class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(h)-1
        maxi=0
        while(i<j):
            mini=min(h[i],h[j])
            area=mini*(j-i)
            maxi=max(maxi,area)
            if(h[i]<h[j]):
                i+=1
            else:
                j-=1
        return maxi

        