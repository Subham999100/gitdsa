class Solution {
    public int countDistinctIntegers(int[] nums) {
        HashSet<Integer> map=new HashSet<>();
        for(int n:nums){
            map.add(n);
            int m=reverse(n);
            if(!map.contains(m)){
                map.add(m);
            }
        }
        return map.size();
    }
    private int reverse(int n){
        int rev=0;
        while(n>0){
           int temp=n%10;
           rev=rev*10+temp;
           n=n/10;
        }
        return rev;
    }
}