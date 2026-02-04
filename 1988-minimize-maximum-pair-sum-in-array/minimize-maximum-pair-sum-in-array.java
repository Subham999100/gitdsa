class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int i=0;
        int j=nums.length-1;
        int maxi=0;
        while(i<j){
           int cur=0;
           cur=nums[i]+nums[j];
           maxi=Math.max(maxi,cur);
           i++;
           j--;            
        }
        return maxi;
    }
}