class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> res = new ArrayList<>();
        int start = newInterval[0], end = newInterval[1];
        for (int i = 0; i < intervals.length; i++) {
            int newStart = intervals[i][0], newEnd = intervals[i][1];
            if (newEnd < start) {
                res.add(new int[] {newStart, newEnd});
            } else if (end < newStart) {
                res.add(new int[] {start, end});
                res.add(new int[] {newStart, newEnd});
                while (++i < intervals.length) {
                    res.add(intervals[i]);
                }
                return res.toArray(new int[res.size()][]);
            } else {
                start = Math.min(start, newStart);
                end = Math.max(end, newEnd);
            }
        }
        res.add(new int[] {start, end});
        return res.toArray(new int[res.size()][]);
    }
}