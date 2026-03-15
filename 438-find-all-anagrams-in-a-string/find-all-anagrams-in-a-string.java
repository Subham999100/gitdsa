import java.util.*;

class Solution {

    public boolean check(String kk, String sortedP){

        char[] arr = kk.toCharArray();
        Arrays.sort(arr);

        return new String(arr).equals(sortedP);
    }

    public List<Integer> findAnagrams(String s, String p) {

        List<Integer> lst = new ArrayList<>();

        int k = p.length();
        int i = 0;

        char[] pArr = p.toCharArray();
        Arrays.sort(pArr);
        String sortedP = new String(pArr);

        StringBuilder sb = new StringBuilder();

        for(int j=0;j<s.length();j++){

            sb.append(s.charAt(j));

            if(j-i+1>k){
                sb.deleteCharAt(0);
                i++;
            }

            if(j-i+1==k){

                if(check(sb.toString(),sortedP)){
                    lst.add(i);
                }
            }
        }

        return lst;
    }
}