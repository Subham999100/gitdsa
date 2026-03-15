class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int i=0;
        double sum=0;
        double maxavg=Integer.MIN_VALUE;
        for(int j=0;j<nums.length;j++){
            sum+=nums[j];
            if(j-i+1>k){
                sum-=nums[i];
                i++;
            }
            if(j-i+1==k){
                double avg=sum/k;
                maxavg=Math.max(avg,maxavg);
            }
            
        }
        return maxavg;
    }
}