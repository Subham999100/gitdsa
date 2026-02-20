class Solution {
    public int findDuplicate(int[] nums) {
        HashSet<Integer> map=new HashSet<>();
        for(int  n:nums){
            if(map.contains(n)){
                return n;
            }
            map.add(n);
        }
        return -1;
    }
}