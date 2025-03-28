class Solution {
    public boolean canConstruct(String s, int k) {
        int len = s.length();
        if (len < k) {
            return false;
        }
        Map<Character, Integer> hashmap = new HashMap<>();
        for (char ch : s.toCharArray()) {
            hashmap.put(ch, hashmap.getOrDefault(ch, 0) + 1);
        }
        int oddNums = 0;
        for (int count : hashmap.values()) {
            if (count % 2 == 1) {
                oddNums++;
            }
        }
        return oddNums <= k;
    }
}