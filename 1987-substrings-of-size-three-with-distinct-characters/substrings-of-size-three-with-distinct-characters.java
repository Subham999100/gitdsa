class Solution {
    public boolean unique(String kk){
        int[] freq=new int[26];
        for(int i=0;i<kk.length();i++){
            char ch=kk.charAt(i);
            freq[ch-'a']++;
        }
        for(int n:freq){
            if(n>1){
                return false;
            }
        }
        return true;
    }
    public int countGoodSubstrings(String s) {
        int k=3;
        int i=0;
        int count=0;
        StringBuilder sb=new StringBuilder();
        for(int j=0;j<s.length();j++){
            char ch=s.charAt(j);
            sb.append(ch);
            if(j-i+1>k){
                sb.deleteCharAt(0);
                i++;
            }
            if(j-i+1==k){
               String kk=sb.toString();
               if(unique(kk)){
                 count++;
               }
            }
        }
        return count;
    }
}