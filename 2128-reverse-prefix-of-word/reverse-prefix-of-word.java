class Solution {
    public String reversePrefix(String word, char ch) {
       int count=0;
       String w=word;
       StringBuffer sb=new StringBuffer();
       for(int i=0;i<word.length();i++){
            char c=word.charAt(i);
            if(c==ch){
                count=i+1;
                break;
            }
       }
       if(count==0){
           return word;
       }
       int mm=count;
       for(int j=count-1;j>=0;j--){
            char kk=word.charAt(j);
            sb.append(kk);
       }
       for(int l=mm;l<word.length();l++){
            char s=word.charAt(l);
            sb.append(s);
       }

        return sb.toString();
    }
}