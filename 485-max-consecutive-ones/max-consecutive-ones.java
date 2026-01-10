class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int r=0;
        int cur=0;
        int maxlen=0;
        while(r<nums.length){
           if(nums[r]==1){
              cur++;
              maxlen=Math.max(maxlen,cur);
           }
           if(nums[r]==0){
             cur=0;
           }
           r++;
        }
        return maxlen;
    }
}