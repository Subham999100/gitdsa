class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int i=0;
        int j=0;
        int count=0;
        int sum=0;
        int tar=threshold*k;
        while(j<arr.length){
            sum+=arr[j];
            if(j-i+1==k){
                if(sum>=tar){
                    count++;
                }
                sum-=arr[i];
                i++;
            }
            j++;
        }
        return  count;
    }
}