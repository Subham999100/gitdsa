class Solution {
    public int[] sortedSquares(int[] nums) {
       int[] copy=new int[nums.length];
       for(int i=0;i<nums.length;i++){
           copy[i]=nums[i]*nums[i];
       } 
        Arrays.sort(copy);
        return copy;
    }
}