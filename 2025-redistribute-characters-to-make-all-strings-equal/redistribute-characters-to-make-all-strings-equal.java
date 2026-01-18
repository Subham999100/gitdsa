class Solution {
    public boolean makeEqual(String[] words) {
        HashMap<Character, Integer> freq = new HashMap<>();
        for (String n : words) {
            for (int i = 0; i < n.length(); i++) {
                char ch = n.charAt(i);
                freq.put(ch, freq.getOrDefault(ch, 0) + 1);
            }
        }
        int n = words.length;
        for (char ch : freq.keySet()) {
            int ok = freq.get(ch);
            if (ok % n != 0) {
                return false;
            }
        }
        return true;
    }
}