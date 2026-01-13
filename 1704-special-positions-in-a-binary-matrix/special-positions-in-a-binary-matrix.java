class Solution {
    public int numSpecial(int[][] mat) {
        int row=mat.length;
        int col=mat[0].length;
        int[] rarr =new int[row];
        int[] carr=new int[col];
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                 if(mat[i][j]==1){
                    rarr[i]++;
                    carr[j]++;
                }
            }
        }
        int count=0;
        for(int i=0;i<rarr.length;i++){
            for(int j=0;j<carr.length;j++){
                if(mat[i][j]==0){
                    continue;
                }
                if(rarr[i]==1&&carr[j]==1){
                    count++;
                }
            }
        }
        return count;
    }
}