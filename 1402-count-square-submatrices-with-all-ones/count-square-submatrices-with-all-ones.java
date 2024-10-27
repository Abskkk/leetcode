class Solution {
    public int countSquares(int[][] matrix) {
        int[][] dp = new int[matrix.length + 1][matrix[0].length + 1];
        int res = 0;
        for (int i = matrix.length - 1; i >= 0; i--) {
            for (int j = matrix[0].length - 1; j >= 0; j--) {
                if (matrix[i][j] == 1) {
                    dp[i][j] = Math.min(Math.min(dp[i][j + 1], dp[i + 1][j]), dp[i + 1][j + 1]) + 1;
                    res += dp[i][j];
                }

            }
        }
        return res;
    }
}