class Solution(object):
    def maxProfit(self, p):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxpro=0
        buy=p[0]
        for i in range(len(p)):
            if p[i]<buy:
                buy=p[i]
            if p[i]>buy:
                maxpro=max(maxpro,p[i]-buy)
        return maxpro
   