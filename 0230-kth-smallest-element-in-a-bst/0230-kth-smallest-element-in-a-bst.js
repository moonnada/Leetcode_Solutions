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
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    /*
    1. make a func to in-order setting
    2. to iterate the sorted arr to return the 'k' smallest
    */
    
    if(!root) return -1;
    let sorted = [];
    inOrder(root);
    
    function inOrder(node){
        if(!node) return;
        if(node.left) inOrder(node.left);
        sorted.push(node.val);
        if(node.right) inOrder(node.right)
        
    }
    
    return sorted[k-1]
};