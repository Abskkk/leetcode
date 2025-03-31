class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        List<int[]> res = new ArrayList<>();
        int prevStart = intervals[0][0], prevEnd = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            int start = intervals[i][0], end = intervals[i][1];
            if (start <= prevEnd) {
                prevEnd = Math.max(prevEnd, end);
            } else {
                res.add(new int[]{prevStart, prevEnd});
                prevStart = start;
                prevEnd = end;
            }
        }
        res.add(new int[]{prevStart, prevEnd});
        return res.toArray(new int[res.size()][]);
    }
}