class Solution {
    public int maxArea(int[] h) {
        int i=0;
        int j=h.length-1;
        int maxi=Integer.MIN_VALUE;
        while(i<j){
            int wid=j-i;
            int hei=Math.min(h[i],h[j]);
            int area=wid*hei;
            maxi=Math.max(area,maxi);
            if(h[i]<h[j]){
                i++;
            }else{
                j--;
            }
        }
        return maxi;
    }
}