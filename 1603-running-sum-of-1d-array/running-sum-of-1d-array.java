class Solution {
    public int[] runningSum(int[] nums) {
        int tsum=0;
        for(int i=0;i<nums.length;i++){
            if(i==0){
                tsum=nums[0];
            }else{
             tsum+=nums[i];
            }
            if(i>0){
                nums[i]=tsum;
            }
        }
        return nums;
    }
}