class Solution {
    int[] candidates;
    int target;
    List<List<Integer>> res;
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        this.candidates = candidates;
        this.target = target;
        res = new ArrayList<>();
        backTrack(0, 0, new ArrayList<>());
        return res;
    }
    private void backTrack(int i, int sum, List<Integer> curr) {
        if (sum > target) {
            return ;
        }
        if (i == candidates.length) {
            if (target == sum) {
                res.add(new ArrayList<>(curr));
            }
            return ;
        }
        backTrack(i + 1, sum, curr);
        curr.add(candidates[i]);
        backTrack(i, sum + candidates[i], curr);
        curr.remove(curr.size() - 1);
    }
}