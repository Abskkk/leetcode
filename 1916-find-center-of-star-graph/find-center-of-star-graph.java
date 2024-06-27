class Solution {
    public int findCenter(int[][] edges) {
        Set<Integer> hashSet = new HashSet<>();
        for (int[] nodes : edges) {
            int node1 = nodes[0], node2 = nodes[1];
            if (hashSet.contains(node1)) return node1;
            if (hashSet.contains(node2)) return node2;
            hashSet.add(node1);
            hashSet.add(node2);
        }
        return -1;
    }
}