class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int l=0;
        int r=0;
        int cur=0;
        int maxlen=0;
        while(r<nums.length){
           if(nums[r]==1){
              cur++;
              maxlen=Math.max(maxlen,cur);
           }
           if(nums[r]==0){
             l=r;
             cur=0;
           }
           r++;
        }
        return maxlen;
    }
}