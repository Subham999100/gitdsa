class Solution(object):
    def findMaxAverage(self, nums, k):

        curr_sum = 0
        i = j = 0
        max_sum = float('-inf')

        while j < len(nums):

            curr_sum += nums[j]

            if j - i + 1 < k:
                j += 1

            elif j - i + 1 == k:

                max_sum = max(max_sum, curr_sum)

                curr_sum -= nums[i]
                i += 1
                j += 1

        return max_sum / float(k)