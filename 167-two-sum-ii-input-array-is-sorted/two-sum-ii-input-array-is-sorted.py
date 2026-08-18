class Solution(object):
    def twoSum(self, n, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(n)-1
        while(i<j):
            s=n[i]+n[j]
            if(s==target):
                return [i+1,j+1]
            elif(s>target):
                j-=1
            else:
                i+=1
        
