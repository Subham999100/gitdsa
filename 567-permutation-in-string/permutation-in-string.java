class Solution {
    public boolean check(String kk,String s){
        int[] freq=new int[26];
        for(int i=0;i<s.length();i++){
            char ch=kk.charAt(i);
            char kh=s.charAt(i);
            freq[ch-'a']++;
            freq[kh-'a']--;
        }
        for(int n:freq){
            if(n>0){
                return false;
            }
        }
        return true;
    }
    public boolean checkInclusion(String s1, String s2) {
        int k=s1.length();
        int i=0;
        StringBuilder sb=new StringBuilder();
        for(int j=0;j<s2.length();j++){
            char ch=s2.charAt(j);
            sb.append(ch);
            if(j-i+1>k){
                sb.deleteCharAt(0);
                i++;
            }
            if(j-i+1==k){
                String kk=sb.toString();
                if(check(kk,s1)){
                    return true;
                }
            }
        }
        return false;
    }
}