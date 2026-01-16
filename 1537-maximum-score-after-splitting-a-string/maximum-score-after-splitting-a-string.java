class Solution {
        public int findone(String kk){
        int count=0;
        for(int i=0;i<kk.length();i++){
            char ch=kk.charAt(i);
            int ok=ch-'0';
            if(ok==1){
                count++;
            }
        }
        return count;
    }
    public int maxScore(String s) {
        int maxi=0;
        int curr=0;
        String left="";
        String right="";
        int l=0;
        int r=0;
        int n=s.length();
        int cou=0;
        for(int i=0;i<s.length()-1;i++){
            char ch=s.charAt(i);
            if(ch-'0'==0){
                cou++;
            }
            left+=ch;
            right+=s.substring(i+1,n);
            l=cou;
            r=findone(right);
            curr=l+r;
            maxi=Math.max(curr,maxi);
            curr=0;
            left="";
            right="";
        }
        return maxi;
    }
}