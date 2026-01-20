class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        HashSet<Integer> map=new HashSet<>();
        for(int n:nums1){
            map.add(n);
        }
        int mini=Integer.MAX_VALUE;
        for(int n:nums2){
            if(map.contains(n)){
                mini=Math.min(mini,n);
            }
        }
        return mini==Integer.MAX_VALUE? -1: mini;
    }
}