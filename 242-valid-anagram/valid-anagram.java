class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer>fre =new HashMap<>();
        if(s.length()!=t.length()){
            return false;
        }
        for(char c:s.toCharArray()){
            fre.put(c,fre.getOrDefault(c,0)+1);
        }
        for(char c:t.toCharArray()){           
            if(fre.containsKey(c) && fre.get(c)>0){ 
                fre.put(c,fre.get(c)-1);
            }
        }
        for(char n:fre.keySet()){
             if(fre.get(n)>0){
                return false;
             }
        }
        return true;
    }
}