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
        for(int i=n-1;i>=0;i--){
            if(i==n-1){
                sb.append('1');
                one--;
            }
            if(zero!=0){
                sb.append('0');
                zero--;
            }
            if(zero==0 && one>0){
                sb.append('1');
                one--;
            }
        }
        return sb.reverse().toString();


    }
}