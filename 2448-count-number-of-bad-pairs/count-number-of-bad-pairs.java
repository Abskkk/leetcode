class Solution {
    public long countBadPairs(int[] nums) {
        Map<Integer, Integer> hashmap = new HashMap<>();
        long res = 0;
        for (int i = 0; i < nums.length; i++) {
            int val = nums[i] - i;
            res += i - hashmap.getOrDefault(val, 0);
            hashmap.put(val, hashmap.getOrDefault(val, 0) + 1);
        }
        return res;
    }
}