class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> map=new HashSet<>();
        for(int n:nums1){
            map.add(n);
        }
        HashSet<Integer> result=new HashSet<>();
        for(int n:nums2){
            if(map.contains(n)){
                result.add(n);
            }
        }
        int[] res=new int[result.size()];
        int i=0;
        for(int n:result){
            res[i++]=n;
        }
        return res;
    }
}