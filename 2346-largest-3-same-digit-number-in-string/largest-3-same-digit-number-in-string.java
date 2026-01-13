class Solution {
    public String largestGoodInteger(String num) {
        int best=-1;
        for(int i=0;i<=num.length()-3;i++){
            char ch=num.charAt(i);
            if(ch==num.charAt(i+1)&&ch==num.charAt(i+2)){
                best=Math.max(best,ch-'0');
            }
        }
        return best==-1?"":""+best+best+best;
    }
}