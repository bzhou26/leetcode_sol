/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        return dfs(root, 0);
    }
    public int dfs(TreeNode root, int level){
        if (root != null) {
            return Math.max(dfs(root.left, level + 1), dfs(root.right, level + 1));
        }
        return level;
    }
}