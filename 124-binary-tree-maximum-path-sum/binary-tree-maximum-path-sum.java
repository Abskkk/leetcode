/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int res;
    public int maxPathSum(TreeNode root) {
        res = root.val;
        maxDepth(root);
        return res;
    }

    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = Math.max(maxDepth(root.left), 0), right = Math.max(maxDepth(root.right), 0);
        int depth = Math.max(root.val + left, root.val + right);
        res = Math.max(res, root.val + right + left);
        return depth;
    }
}