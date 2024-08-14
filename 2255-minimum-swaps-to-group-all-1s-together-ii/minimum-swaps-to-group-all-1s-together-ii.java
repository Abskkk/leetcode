// '''
// count 1'. n
// prefixSum
// prefix[i + n] - prefix[i] maxmum of numbers of 1
// '''
// nums = nums + nums;


class Solution {
    public int minSwaps(int[] nums) {
        int[] newNums = new int[nums.length * 2];
        for (int i = 0; i < nums.length; i++) {
            newNums[i] = nums[i];
            newNums[i + nums.length] = nums[i];
        }
        int[] prefix = new int[nums.length * 2];
        int numOfOne = 0;
        for (int i = 0; i < newNums.length; i++) {
            if (newNums[i] == 1) {
                numOfOne++;
            }
            prefix[i] = numOfOne;
        }
        numOfOne /= 2;
        if (numOfOne == 0) return 0;
        int max = 0;
        for (int j = 0; j < newNums.length - numOfOne; j++) {
            int temp = j != 0 ? prefix[j - 1] : 0;
            max = Math.max(max, prefix[j + numOfOne - 1] - temp);
        }
        return numOfOne - max;
    }
}