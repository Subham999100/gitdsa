class Solution {
    public int buyChoco(int[] prices, int money) {
        int min1=Integer.MAX_VALUE;
        int min2=Integer.MAX_VALUE;

        for(int n:prices){
            if(n<min1){
                min2=min1;
                min1=n;
            }else if(n<min2){
                min2=n;
            }
        }
        int ok=money;
        int count=0;
        if(min1<money){
            money-=min1;
            count++;
        }
        if(min2<=money){
            money-=min2;
            count++;
        }
        return count==2 ? money:ok;
    }
}