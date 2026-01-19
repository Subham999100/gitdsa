class Solution {
    public int missingNumber(int[] nums) {
        int n=nums.length;
        int exp=n*(n+1)/2;
        int act=0;
        for(int k:nums){
            act+=k;
        }
        return exp-act;
    }
}