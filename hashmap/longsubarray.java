package hashmap;
import java.util.*;

public class longsubarray {
    static int lng(int[] nums,int k){
        HashMap<Integer,Integer> freq=new HashMap<>();
        int sum=0;
        int maxlen=0;
        for(int i=0;i<nums.length;i++){
            sum+=nums[i];
            int comp=sum-k;
            if(sum==k){
                maxlen=i+1;
            }
            if(freq.containsKey(comp)){
                int length=i-freq.get(comp);
                maxlen=Math.max(maxlen,length);
            }
            if(!freq.containsKey(comp)){
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
        int k=sc.nextInt();
        int res=lng(arr, k);
        System.out.println("longest max length"+res);
    }
    
}
