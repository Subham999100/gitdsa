class Solution(object):
    def bin(self,i,j,arr,tar):
        mid=(i+j)//2        
        if i>j:
            return -1
        if(arr[mid]<tar):
            return self.bin(mid+1,j,arr,tar)
        if(arr[mid]>tar):
            return self.bin(i,mid-1,arr,tar)
        if(arr[mid]==tar):
            return mid

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        j=len(nums)-1
        return self.bin(i,j,nums,target)

        