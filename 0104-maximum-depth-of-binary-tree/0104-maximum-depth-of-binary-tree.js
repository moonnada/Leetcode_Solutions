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
var maxDepth = function(root) {
    /*
    dfs
    1. check a null case
    2. make a func to count depth
    3. get the max depth to compare 
    */
    
    if(!root) return 0;
    let left = maxDepth(root.left);
    let right = maxDepth(root.right);
    
    return Math.max(left, right) + 1
    
};
