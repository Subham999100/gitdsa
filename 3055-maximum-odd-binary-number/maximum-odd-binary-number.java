class Solution {
    public String maximumOddBinaryNumber(String s) {
        int one=0;
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            int x=ch-'0';
            if(x==1){
                one++;
            }
        }
        int n=s.length();
        int zero=n-one;
        StringBuilder sb=new StringBuilder();
        for(int i=0;i<one-1;i++){
            sb.append('1');
        }
        for(int i=0;i<zero;i++){
            sb.append('0');
        }
        sb.append('1');
        return sb.toString();
    }
}