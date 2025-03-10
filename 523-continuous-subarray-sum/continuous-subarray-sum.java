class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        Map<Integer, Integer> prifix = new HashMap<>();
        prifix.put(0, -1);
        int currMod = 0;
        for (int i = 0; i < nums.length; i++) {
            currMod = (currMod + nums[i]) % k;
            if (prifix.containsKey(currMod) && i - prifix.get(currMod) >= 2) {
                return true;
            }
            if (!prifix.containsKey(currMod)) {
                prifix.put(currMod, i);
            }
        }
        return false;
    }
}