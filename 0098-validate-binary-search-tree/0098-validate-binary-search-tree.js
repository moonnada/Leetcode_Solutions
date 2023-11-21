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
var isValidBST = function(root) {
    /*
    dfs using recursion
        1. in a helper func, check bst or not
    */
    
    if(!root) return false;
    if(root.length === 1) return true;
    
    return checkValid(root, -Infinity, Infinity);
    
    function checkValid(node, lower, upper){
        if(!node) return true;
        if((lower < node.val) && (upper > node.val)){
            return checkValid(node.left, lower, node.val) && checkValid(node.right, node.val, upper)
        } else return false
    }
};