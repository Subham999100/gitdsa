class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minpri=prices[0]
        maxi=0
        for  i in range(len(prices)):
            if minpri>prices[i]:
                minpri=prices[i]
            else:
                pro=prices[i]-minpri
                maxi=max(maxi,pro)
        return maxi