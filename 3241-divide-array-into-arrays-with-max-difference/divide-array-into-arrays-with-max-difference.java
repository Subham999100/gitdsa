class Solution {
    public int[][] divideArray(int[] nums, int k) {
        Arrays.sort(nums);
        int n=nums.length;
        int[][] result=new int[n/3][3];
        int idx=0;
        for(int i=0;i<nums.length;i+=3){
            if(nums[i+2]-nums[i]>k){
                return new int[0][0];  
            }
            result[idx][0]=nums[i];
            result[idx][1]=nums[i+1];
            result[idx][2]=nums[i+2];
            idx++;

        }
        return result;
    }
}