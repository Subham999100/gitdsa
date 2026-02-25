class Solution {
    public int pivotIndex(int[] nums) {
        int totalsum=0;
        for(int n:nums){
            totalsum+=n;
        }
        int sum=0;
        for(int i=0;i<nums.length;i++){
            if(2*sum+nums[i]==totalsum){
                return i;
            }
            sum+=nums[i];
        }
        return -1;
    }
}