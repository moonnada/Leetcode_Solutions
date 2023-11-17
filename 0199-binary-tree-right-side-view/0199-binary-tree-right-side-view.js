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
 * @return {number[]}
 */
var rightSideView = function(root) {
    /*
    1. check empty root
    2. 
    */
    
    if(!root) return [];
    let queue = [[root, 0]];
    let ans = [];
    
    while(queue.length){
        let [node, level] = queue.shift();
        if(ans.length === level){
            ans.push(node.val)
        }
        
        node.right && queue.push([node.right, level+1]);
        node.left && queue.push([node.left, level+1])
    }
    return ans
};