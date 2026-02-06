class Solution {
    public boolean allzero(int[] arr){
        for(int i:arr){
            if(i!=0){
                return false;
            }
        }
        return true;
    }
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> lst=new ArrayList<>();
        int[] freq=new int[26];
        for(int i=0;i<p.length();i++){
            char ch=p.charAt(i);
            freq[ch-'a']++;
        }
        int n=s.length();
        int k=p.length();
        int i=0;
        int j=0;
        while(j<n){
            char kk=s.charAt(j);
            freq[kk-'a']--;
            if(j-i+1==k){
                if(allzero(freq)){
                    lst.add(i);
                }
                char ll=s.charAt(i);
                freq[ll-'a']++;
                i++;
            }
            j++;
        }
        return lst;
    }
}