class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        maxi=0
        while(i<j):
            mini=min(height[i],height[j])
            maxi=max(maxi,(j-i)*mini)
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        return maxi
