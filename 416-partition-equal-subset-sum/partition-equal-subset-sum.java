class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        if (sum % 2 == 1) {
            return false;
        }
        Boolean[][] memo = new Boolean[nums.length][sum / 2 + 1];
        return dfs(0, nums, 0, sum, memo);
    }
    private boolean dfs(int i, int[] nums, int curr, int sum, Boolean[][] memo) {
        if (curr == sum / 2) {
            return true;
        }
        if (i == nums.length || curr > sum / 2) {
            return false;
        }
        if (memo[i][curr] != null) {
            return memo[i][curr];
        }
        memo[i][curr] = dfs(i + 1, nums, curr + nums[i], sum, memo) || dfs(i + 1, nums, curr, sum, memo);
        return memo[i][curr];
    }
}