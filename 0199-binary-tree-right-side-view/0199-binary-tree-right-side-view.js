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
    if(!root) return [];
    let queue = [[root, 0]];
    let ans = [];
    
    while(queue.length){
        let [curNode, level] = queue.shift();
        if(ans.length === level) ans.push(curNode.val);
        
        if(curNode.right) queue.push([curNode.right, level+1])
        if(curNode.left) queue.push([curNode.left, level+1]);
        

    }
    return ans
       
        
    
};