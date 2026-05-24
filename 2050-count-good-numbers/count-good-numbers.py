class Solution(object):
    m=1000000007
    def findpow(self,a,b):
        if(b==0):
            return 1
        half=self.findpow(a,b//2)
        result=(half*half)%self.m
        if(b%2==1):
            result=(result*a)%self.m
        return result
    def countGoodNumbers(self, n):
        return (self.findpow(5,(n+1)//2)* self.findpow(4,n//2))%self.m