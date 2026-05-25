class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        nega=False
        if(n<0):
            n=-(n)
            nega=True
        if(n==0):
            return 1
        half=self.myPow(x,n//2)
        result=half*half
        if(n%2==1):
            result=result*x
        if(nega==True):
            return 1/result
        return result
        