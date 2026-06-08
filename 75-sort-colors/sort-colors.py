class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def mergesort(arr,low,high):
            if(low>=high):
                return
            mid=(low+high)//2
            mergesort(arr,low,mid)
            mergesort(arr,mid+1,high)
            merge(arr,low,mid,high)
        def merge(arr,low,mid,high):
            left=low
            right=mid+1
            temp=[]
            while(left<=mid and right<=high):
                if arr[left]<=arr[right]:
                    temp.append(arr[left])
                    left+=1
                else:
                    temp.append(arr[right])
                    right+=1
            while(left<=mid):
                temp.append(arr[left])
                left+=1
            while(right<=high):
                temp.append(arr[right])
                right+=1
            for i in range(len(temp)):
                arr[low+i]=temp[i]
        
        mergesort(nums,0,len(nums)-1)