class Solution {
    public int maximumCount(int[] nums) {
        return Math.max(numOfNeg(nums), NumOfPos(nums));
    }
    private int NumOfPos(int[] nums) {
        int left = 0, right = nums.length - 1;
        int index = nums.length;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] <= 0) {
                left = mid + 1;
            } else if (nums[mid] > 0) {
                right = mid - 1;
                index = mid;
            }
        }
        return nums.length - index;
    }
    private int numOfNeg(int[] nums) {
        int left = 0, right = nums.length - 1;
        int index = -1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] >= 0) {
                right = mid - 1;
            } else if (nums[mid] < 0) {
                left = mid + 1;
                index = mid;
            }
        }
        return index + 1;
    }
}