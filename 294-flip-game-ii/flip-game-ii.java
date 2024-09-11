class Solution {
    public boolean canWin(String currentState) {
        return dfs(currentState.toCharArray());
    }
    public boolean dfs(char[] chars) {
        char prev = '*';
        boolean flag = false;
        for (char ch : chars) {
            if (ch == '+' && prev == '+') {
                flag = true;
            }
            prev = ch;
        }
        if (flag == false) {
            return false;
        }

        prev = '*';
        for (int i = 0; i < chars.length; i++) {
                char ch = chars[i];
                if (ch == '+' && prev == '+') {
                    chars[i] = '-';
                    chars[i - 1] = '-';
                    if (!dfs(chars)) {
                        chars[i] = '+';
                        chars[i - 1] = '+';
                        return true;
                    }
                    chars[i] = '+';
                    chars[i - 1] = '+';
                }
                prev = ch;
            }
            return false;
        }
    }
