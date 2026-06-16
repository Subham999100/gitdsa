class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        di={}
        for num in nums:
            di[num]=di.get(num,0)+1
        freq=[]
        for i in range(len(nums)+1):
            freq.append([])
        for num,ind in di.items():
            freq[ind].append(num)
        res=[]
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                res.append(num)
                k-=1

                if k==0:
                    return res

        