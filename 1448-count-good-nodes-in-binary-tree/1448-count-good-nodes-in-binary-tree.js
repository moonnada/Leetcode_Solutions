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
    bfs
    
    1. check edge case(empty, one node)
    2. init a cnt val
    3. init a helper func(node)
    4. return cnt
    
    5. in a helper func, 
        5.1) if node not exists, return;
        5.2) check curNode.val <= root.val. if it is cnt++
        5.3) visit left and right side recursively
    */
    
    if(!root) return;
    let cnt = 1;
    helper(root.left, root.val);
    helper(root.right, root.val)
    return cnt;
    
    function helper(node, maxVal){
        if(!node) return;
        if(node.val >= maxVal) cnt++;
        
        helper(node.left, Math.max(maxVal, node.val));
        helper(node.right, Math.max(maxVal, node.val))
    }
};