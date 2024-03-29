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
 * @return {boolean}
 */
var isBalanced = function(root) {
    if(!root) return true;
    return Math.abs( maxHeight(root.left) - maxHeight(root.right)) < 2 && isBalanced(root.left) && isBalanced(root.right);
    
    function maxHeight(root){
        if(!root) return -1;
        return 1 + Math.max(maxHeight(root.left), maxHeight(root.right))
    }
};