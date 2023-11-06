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
 * @return {TreeNode}
 */
var invertTree = function(root) {
    
//     if(!root) return root;
//     let left = invertTree(root.left);
//     let right = invertTree(root.right);
//     root.left = right;
//     root.right = left;
//     return root
 
    
    let queue = [root];
    if(!queue) return root;
    
    while(queue.length){
        let curVal = queue.pop();
        if(curVal){
               let tmp = curVal.left;
        curVal.left = curVal.right;
        curVal.right = tmp;
        
     
        
        if(curVal.left) queue.push(curVal.left);
        if(curVal.right) queue.push(curVal.right);
        }
        
    }
    return root
}
