class Solution {
    public int maximumProduct(int[] n) {
        int m=n.length-1;
        Arrays.sort(n);
        int mul=Math.max(n[m]*n[m-1]*n[m-2],n[0]*n[1]*n[m]);
        return mul;
    }
}