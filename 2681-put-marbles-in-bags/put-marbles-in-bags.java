class Solution {
    public long putMarbles(int[] weights, int k) {
        int[] pairs = new int[weights.length - 1];
        for (int i = 0; i < weights.length - 1; i++) {
            pairs[i] = weights[i] + weights[i + 1];
        }
        Arrays.sort(pairs);
        long minSum = 0, maxSum = 0;
        for (int j = 0; j < k - 1; j++) {
            minSum += pairs[j];
        }
        for (int m = 0; m < k - 1; m++) {
            maxSum += pairs[pairs.length - 1 - m];
        }
        return maxSum - minSum;
    }
}