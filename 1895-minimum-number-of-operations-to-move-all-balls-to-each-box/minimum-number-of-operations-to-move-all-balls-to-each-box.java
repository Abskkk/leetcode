class Solution {
    public int[] minOperations(String boxes) {
        int[] prefix = new int[boxes.length()];
        int[] suffix = new int[boxes.length()];
        int[] res = new int[boxes.length()];
        int ballToLeft = 0, moveToLeft = 0, ballToRight = 0, moveToRight = 0;
        for (int i = 0; i < boxes.length(); i++) {
            moveToLeft = i == 0 ? 0 : moveToLeft + ballToLeft;
            prefix[i] = moveToLeft;
            ballToLeft += Character.getNumericValue(boxes.charAt(i));
        }
        for (int i = boxes.length() - 1; i >= 0; i--) {
            moveToRight = i == boxes.length() - 1 ? 0 : moveToRight + ballToRight;
            suffix[i] = moveToRight;
            ballToRight += Character.getNumericValue(boxes.charAt(i));
        }
        for (int i = 0; i < boxes.length(); i++) {
            res[i] = prefix[i] + suffix[i];
        }
        return res;
    }
}