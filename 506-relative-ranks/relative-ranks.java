class Solution {
    public String[] findRelativeRanks(int[] score) {

        int n = score.length;

        // convert to Integer[]
        Integer[] copy = new Integer[n];
        for (int i = 0; i < n; i++) {
            copy[i] = score[i];
        }

        // sort ONCE
        Arrays.sort(copy, Collections.reverseOrder());

        // map score -> rank
        Map<Integer, Integer> rankMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            rankMap.put(copy[i], i + 1);
        }

        // build answer
        String[] ranki = new String[n];
        for (int i = 0; i < n; i++) {
            int ran = rankMap.get(score[i]);

            if (ran == 1) {
                ranki[i] = "Gold Medal";
            } else if (ran == 2) {
                ranki[i] = "Silver Medal";
            } else if (ran == 3) {
                ranki[i] = "Bronze Medal";
            } else {
                ranki[i] = String.valueOf(ran);
            }
        }

        return ranki;
    }
}
