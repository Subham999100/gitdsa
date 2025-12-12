package hashmap;
import java.util.*;

public class longseq {
    static int seq(int[] nums){
        HashSet<Integer> freq=new HashSet<>();
        int maxlen=0;
        
        for(int n:nums){
            freq.add(n);
        }
        for(int n:freq){
            if(!freq.contains(n-1)){
                int start=n;
                int lenght=1;
                while(freq.contains(start+1)){
                    lenght++;
                    start++;
                    maxlen=Math.max(lenght, maxlen);
                }
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
        int res=seq(arr);
        System.out.println(res);
    }  
}
