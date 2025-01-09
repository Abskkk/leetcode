class Solution {
    public int prefixCount(String[] words, String pref) {
        int res = 0;
        for (String word : words) {
            if (containPrefix(word, pref)) {
                res++;
            };
        }
        return res;
    }
    public boolean containPrefix(String word, String pref) {
        if (pref.length() > word.length()) {
            return false;
        }
        for (int i = 0; i < pref.length(); i++) {
            if (word.charAt(i) != pref.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}