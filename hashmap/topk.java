package hashmap;
import java.util.*;
public class topk {
    public int[] kfrequent(int[] arr,int k){
        HashMap<Integer,Integer> freq=new HashMap<>();
        for(int num:arr){
            freq.put(num,freq.getOrDefault(num,0)+1);
        }
        List<Integer>[] bucket=new List[arr.length+1];
        for(int key:freq.keySet()){
            int frequency=freq.get(key);
            if(bucket[frequency]==null){
                bucket[frequency]=new ArrayList<>();
            }
            bucket[frequency].add(key); 
        }
        int count=0;
        int[] res=new int[k];
        for(int i=bucket.length-1;i>=0 && count<k;i--){
            if(bucket[i]!=null){
                for(int o:bucket[i]){
                    res[count++]=o;
                }
            }
        }
        return res;

    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        int[] arr=new int[x];
        for(int i=0;i<x;i++){
            arr[i]=sc.nextInt();
        }
        int k=sc.nextInt();
        topk obj=new topk();
        int[] result=obj.kfrequent(arr, k);
        for(int r:result){
            System.out.print(r+"    ");
        }
    }
}
