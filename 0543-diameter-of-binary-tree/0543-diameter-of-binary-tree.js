/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var diameterOfBinaryTree = function(root) {
    /*
    DFS
    
    1. in a helper func, if root not exist, return 0
    2. else 1 + helper func
    */
    
    if(!root) return 0;
    let max = 0;
    dfs(root);
    
    return max;
    
    function dfs(root){
        if(!root) return 0;
        let left = dfs(root.left);
        let right = dfs(root.right);
        max = Math.max(left+ right, max);
        return Math.max(right, left) + 1
    }
};