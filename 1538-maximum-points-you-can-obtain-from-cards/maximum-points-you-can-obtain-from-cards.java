class Solution {
    public int maxScore(int[] c, int k) {
        int n=c.length;
        int leftsm=0;
        for(int i=0;i<k;i++){
            leftsm+=c[i];
        }
        int max=leftsm;
        int rightsum=0;
        for(int j=1;j<=k;j++){
            leftsm-=c[k-j];
            rightsum+=c[n-j];
            max=Math.max(max,rightsum+leftsm);
        }
        return max;
    }
}