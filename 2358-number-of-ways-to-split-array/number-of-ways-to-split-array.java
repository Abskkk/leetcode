class Solution {
    public int waysToSplitArray(int[] nums) {
        long[] prefix = new long[nums.length];
        long prev = 0;
        for (int i = 0; i < nums.length; i++) {
            prefix[i] = prev + nums[i];
            prev = prefix[i];
        }
        long sum = prefix[nums.length - 1];
        int res = 0;
        for (int j = 0; j < nums.length - 1; j++) {
            if (prefix[j] >= sum - prefix[j]) {
                res++;
            }
        }
        return res;
    }
}