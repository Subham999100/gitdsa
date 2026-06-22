class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(h)-1
        maxi=0
        while i<j:
            sur=min(h[i],h[j])
            maxi=max(maxi,(j-i)*sur)
            if (h[i]<h[j]):
                i+=1
            else:
                j-=1
        return maxi