class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        HashMap<Character,Integer> freq=new HashMap<>();
        int max=-1;
        int maxlen=-1;
        int j=0;
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            if(freq.containsKey(ch)){
                j=freq.get(ch);
                max=i-j-1;
                maxlen=Math.max(maxlen,max);
            }else{
                freq.put(ch,i);
            }
        }
        return maxlen;
    }
}