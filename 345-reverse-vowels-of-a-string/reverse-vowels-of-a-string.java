class Solution {
    public boolean isvow(char c){
        if((c=='A'||c=='E'||c=='I'||c=='O'||c=='U')||(c=='a'||c=='e'||c=='i'||c=='o'||c=='u')){
            return true;
        }
        return false;
        
    }
    public String reverseVowels(String s) {
        int i=0;
        int j=s.length()-1;
        char[] kk=s.toCharArray();
        while(i<=j){
            if(!isvow(kk[i])){
                i++;
            }else if(!isvow(kk[j])){
                j--;
            }else{
                char tem=kk[i];
                kk[i]=kk[j];
                kk[j]=tem;
                i++;
                j--;
            }
        }
        return new String(kk);
    }
}