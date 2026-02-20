class Solution {
    public int maxProfit(int[] p) {
        int minpri=p[0];
        int maxi=0;
        int cur=0;
        for(int i=1;i<p.length;i++){
            if(minpri>p[i]){
                minpri=p[i];

            }
            cur=p[i]-minpri;
            maxi=Math.max(maxi,cur);
        }
        return maxi;
    }
}