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
var goodNodes = function(root) {
    //dfs
    let cnt = 0;
    // helper(root.left, root.val);
    // helper(root.right, root.val);
    helper(root, root.val)
    return cnt;
    
    function helper(node, maxVal){
        if(!node) return;
        
        if(node.val >= maxVal) cnt++;
        
        helper(node.left, Math.max(node.val, maxVal));
        helper(node.right, Math.max(node.val, maxVal))
    }
    
};