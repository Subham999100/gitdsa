class Solution {
    public String reverseWords(String s) {
        StringBuffer sb=new StringBuffer();
        int j=s.length();
        int i=0;
        while(i<j){
           while(i<j && s.charAt(i)==' '){
              i++;
           }
           if(i>j){
            break;
           }
           int r=i;
           while(i<j && s.charAt(i)!=' '){
              i++;
           }
           int l=i;
           sb.append(new StringBuffer(s.substring(r,l)).reverse());
           sb.append(' ');

        }
        return sb.toString().trim();
    }
}