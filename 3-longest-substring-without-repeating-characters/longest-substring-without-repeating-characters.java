class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l=0;
        int maxlen=0;
        HashMap<Character,Integer> freq=new HashMap<>();
        for(int r=0;r<s.length();r++){
            char ch=s.charAt(r);
            if(freq.containsKey(ch)&& freq.get(ch)>=l){
                l=freq.get(ch)+1;
            }
            freq.put(ch,r);
            maxlen=Math.max(maxlen,r-l+1);


        }
        return maxlen;
    }
}