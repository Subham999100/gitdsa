package hashmap;

import java.util.*;

public class contigousarray {
    static int findsum(int[] nums){
        HashMap<Integer,Integer>freq=new HashMap<>();
        int sum=0;
        int maxlen=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0){
                sum-=1;
            }else{
                sum+=1;
            }
            if(sum==0){
                maxlen=i+1;
            }
            if(freq.containsKey(sum)){
                int len=i-freq.get(sum);
                maxlen=Math.max(maxlen,len);

            }else{
                freq.put(sum,i);
            }
        }
        return maxlen;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        int[] arr=new int[x];
        for(int i=0;i<x;i++){
            arr[i]=sc.nextInt();
        }
        int res=findsum(arr);
        System.out.println(res+"highest lenght of subarray");
    }
}
