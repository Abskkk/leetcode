class Solution {
    public String clearDigits(String s) {
        StringBuilder stack = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (Character.isDigit(ch) && !stack.isEmpty()) {
                stack.setLength(stack.length() - 1);
            } else {
                stack.append(ch);
            }
        }
        return stack.toString();
        }
}