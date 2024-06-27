class Solution {
    int[] nums;
    public int rob(int[] nums) {
        this.nums = nums;
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        return Math.max(robFromStartToEnd(0, nums.length - 2), robFromStartToEnd(1, nums.length - 1));
    }
    
    public int robFromStartToEnd(int start, int end) {
        int first = 0, second = 0;
        for (int i = start; i <= end; i++) {
            int curr = nums[i];
            int temp = second;
            second = Math.max(second, first + curr);
            first = temp;
        }
        return second;
    }
}