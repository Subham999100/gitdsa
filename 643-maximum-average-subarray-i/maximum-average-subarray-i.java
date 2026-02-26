class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int i=0;
        int j=0;
        double avg=0;
        double minavg=Integer.MIN_VALUE;
        double sum=0;
        while(j<nums.length){
            sum+=nums[j];
            if(j-i+1==k){
                avg=sum/k;
                minavg=Math.max(avg,minavg);
                sum-=nums[i];
                i++;
            }
            j++;
        }
        return minavg;
    }
}