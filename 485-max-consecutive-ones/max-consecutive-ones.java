class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int r=0;
        int cur=0;
        int maxlen=0;
        while(r<nums.length){
           if(nums[r]==1){
              cur++;
              maxlen=Math.max(maxlen,cur);
           }else{
            cur=0;
           }
           r++;
        }
        return maxlen;
    }
}