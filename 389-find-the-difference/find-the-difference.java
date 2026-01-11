class Solution {
    public char findTheDifference(String s, String t) {
        int xor=0;
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            xor^=ch;
        }
        for(int i=0;i<t.length();i++){
            char ch=t.charAt(i);
            xor^=ch;
        }
        return (char)xor;
    }
}