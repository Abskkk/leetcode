class Solution {
    public int minOperations(int[] nums, int k) {
        PriorityQueue<Long> pq = new PriorityQueue<>(
            Arrays.stream(nums)
            .mapToLong(i -> (long) i)
            .boxed()
            .collect(Collectors.toList())
        );
        int operation = 0;
        while (pq.peek() < k) {
            long first = pq.poll();
            long second = pq.poll();
            pq.add(first * 2 + second);
            operation++;
        }
        return operation;
    }
}