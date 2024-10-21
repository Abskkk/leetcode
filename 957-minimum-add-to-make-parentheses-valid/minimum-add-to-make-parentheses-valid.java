class Solution {
    public int minAddToMakeValid(String s) {
        int left = 0;
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ')') {
                if (left == 0) {
                    res++;
                } else {
                    left--;
                }
            } else {
                left++;
            }
        }
        res += left;
        return res;
    }
}