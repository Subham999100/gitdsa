class Solution {
    public int characterReplacement(String s, int k) {
        int[] freq=new int[26];
        int l=0;
        int maxfreq=0;
        int maxlen=0;
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            freq[ch-'A']++;
            maxfreq=Math.max(maxfreq,freq[ch-'A']);
            while(i-l+1-maxfreq>k){
                freq[s.charAt(l)-'A']--;
                l++;
            }
            maxlen=Math.max(i-l+1,maxlen);
        }
        return maxlen;
    }
}