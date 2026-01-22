class Solution {
    public int countStudents(int[] st, int[] sa) {
        int cir=0;
        int sq=0;
        for(int m=0;m<st.length;m++){
            if(st[m]==0){
                cir++;
            }else{
                sq++;
            }
        }
        int count=0;
        for(int i:sa){
            if(i==0){
                if(cir==0){
                    break;
                }
                cir--;
            }else{
                if(i==1){
                    if(sq==0){
                        break;
                    }
                    sq--;
                }
            }
        }
        return Math.abs(cir+sq);

    }
}