class Solution {
    public int countCharacters(String[] words, String chars) {
        int[] freq=new int[26];
        for(char c:chars.toCharArray()){
            freq[c-'a']++;
        }
        int total=0;
        for(String w:words){
            int[] temp=freq.clone();
            boolean ok=true;
            for(char c:w.toCharArray()){
                if(temp[c-'a']==0){
                    ok=false;
                    break;
                }
                temp[c-'a']--;
            }
            if(ok){
                total+=w.length();
            }
        }
        return total;
    }
}