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
    Always left child < root.val < right child
    */
    if(!root) return false;
    if(root.length === 1) return true;
    
    return helper(root, -Infinity, Infinity);
    
    function helper(node, minVal, maxVal){
        if(!node) return true;
        
        if((minVal < node.val) && (node.val < maxVal)){
            return helper(node.left,  minVal, node.val) && helper(node.right, node.val, maxVal)
        } return false
    }
};