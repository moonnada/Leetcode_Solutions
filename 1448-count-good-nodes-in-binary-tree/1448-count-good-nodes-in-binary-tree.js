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
    /*
    - only root? cnt++
    
    bfs
    */
    
    if(!root) return 0;
    let cnt = 1;
     helper(root.left, root.val);
    helper(root.right, root.val);
   
    function helper(node, maxVal){
        if(!node) return;
        if(node.val >= maxVal) cnt++;
        
        helper(node.left, Math.max(maxVal, node.val));
        helper(node.right, Math.max(maxVal, node.val))
    }
    
  
    return cnt
};