class Solution {
    public int maxProductDifference(int[] nums) {
        Arrays.sort(nums);
        int n=nums.length;
        int high=nums[n-1]*nums[n-2];
        int low=nums[0]*nums[1];
        return high-low;
    }
}