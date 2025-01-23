class Solution {
    public int[][] highestPeak(int[][] isWater) {
        int[][] dir = new int[][] {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int rows = isWater.length, cols = isWater[0].length;
        int[][] cellHeights = new int[rows][cols];
        for (int[] row : cellHeights) {
            Arrays.fill(row, -1);
        }
        Queue<int[]> cellQueue = new LinkedList<>();

        for (int x = 0; x < rows; x++) {
            for (int y = 0; y < cols; y++) {
                if (isWater[x][y] == 1) {
                    cellQueue.add(new int[] {x, y});
                    cellHeights[x][y] = 0;
                }
            }
        }

        int heightOfNextLayer = 1;
        while (!cellQueue.isEmpty()) {
            int layerSize = cellQueue.size();
            for (int i = 0; i < layerSize; i++) {
                int[] currCell = cellQueue.poll();
                for (int[] d : dir) {
                    int nextX = currCell[0] + d[0];
                    int nextY = currCell[1] + d[1];
                    if (nextX >= 0 && nextX < rows && nextY >= 0 && nextY < cols && cellHeights[nextX][nextY] == -1) {
                        cellHeights[nextX][nextY] = heightOfNextLayer;
                        cellQueue.add(new int[]{nextX, nextY});
                    }
                }
            }
            heightOfNextLayer++;
        }
        return cellHeights;
    }
}