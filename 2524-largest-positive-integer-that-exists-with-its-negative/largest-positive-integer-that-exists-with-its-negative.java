class Solution {
    public int findMaxK(int[] nums) {
        HashSet<Integer> map=new HashSet<>();
        for(int n:nums){
            map.add(n);
        }
        int ans=-1;
        for(int n:nums){
           if(n>0 && map.contains(-n)){
              ans=Math.max(ans,n);
           }
        }
        return ans;
    }
}