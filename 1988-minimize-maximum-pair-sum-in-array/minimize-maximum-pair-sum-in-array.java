class Solution {
    public int minPairSum(int[] nums) {
        int maxi=0;
        int i=0;
        int j=nums.length-1;
        int curr=0;
        Arrays.sort(nums);
        while(i<j){
           curr=nums[i]+nums[j];
           maxi=Math.max(maxi,curr);
           i++;
           j--;
        }
        return maxi;
    }
}