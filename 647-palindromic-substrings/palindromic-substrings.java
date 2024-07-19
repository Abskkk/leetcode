class Solution {
    public int countSubstrings(String s) {
        int n = s.length();
        int res = 0;
        boolean[][] dp = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int l = 0; l < n - i; l++) {
                int r = l + i;
                if (l == r) {
                    dp[l][r] = true;
                    res++;
                } else if (s.charAt(l)==s.charAt(r) && (l == r - 1 || dp[l+1][r-1])) {
                    dp[l][r] = true;
                    res++;
                }
            }
        }
        return res;
    }
}