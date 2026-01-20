class Solution {
    public int maxFrequencyElements(int[] nums) {
        HashMap<Integer,Integer> freq=new HashMap<>();
        int max=0;
        int maxfre=0;
        for(int n:nums){
            freq.put(n,freq.getOrDefault(n,0)+1);
            max=freq.get(n);
            maxfre=Math.max(maxfre,max);
        }
        int count=0;
        for(int n:freq.keySet()){
            int ok=freq.get(n);
            if(ok==maxfre){
                count+=ok;
            }
        }
        return count;

    }
}