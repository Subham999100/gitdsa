class Solution {
    public int firstUniqChar(String s) {
        Map<Character,Integer>freq=new HashMap<>();
        int index=-1;
        for(int i=0;i<s.length();i++){
           char ch=s.charAt(i);
            int frequency=freq.getOrDefault(ch,0);
            freq.put(ch,(frequency+1));
        }
        for(int i=0;i<s.length();i++){
            if(freq.get(s.charAt(i))==1){
                index=i;
                break;
            }
        }
        return index;
    }
}