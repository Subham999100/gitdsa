class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int i=0;
        int j=0;
        int res=0;
        int minlen=Integer.MAX_VALUE;
        

        while(j<nums.length){
           res+=nums[j];
           while(res>=target){
              minlen=Math.min(j-i+1,minlen);
              res-=nums[i];
              i++;
           }
           j++;
        }
        return minlen == Integer.MAX_VALUE ? 0 : minlen;
    }
}