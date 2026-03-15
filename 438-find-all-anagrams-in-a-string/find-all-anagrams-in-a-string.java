class Solution {
    public boolean check(String kk,String p){
        int[] freq=new int[26];
        for(int i=0;i<p.length();i++){
            char ch=kk.charAt(i);
            char kh=p.charAt(i);
            freq[ch-'a']++;
            freq[kh-'a']--;
        }
        for(int n:freq){
            if(n!=0){
                return false;
            }
        }
        return true;
    }
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> lst=new ArrayList<>();
        int k=p.length();
        int i=0;
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
                if(check(kk,p)){
                    lst.add(i);
                }
            }
        }
        return lst;
    }
}