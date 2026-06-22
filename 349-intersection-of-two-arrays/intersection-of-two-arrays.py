class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans=[]
        kick=set()
        for num in nums1:
            kick.add(num)
        for num in nums2:
            if num in kick and num not in ans:
                ans.append(num)
        return ans
        