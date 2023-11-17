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
    2. init a queue and ans
    3. while queue exist
        3.1) shift curNode and curheight from queue
        3.2) if curHeight === ans.length, then put the cur value into ans 
        3.3) if curNode.right exists, put into queue and height++
        3.4) if curNode.left exists, put into queue and height++
    */
    
    if(!root) return [];
    let queue = [[root, 0]];
    let ans = [];
    
    while(queue.length){
        let [curNode, level] = queue.shift();
        
        if(ans.length === level) ans.push(curNode.val);
        
        curNode.right && queue.push([curNode.right, level+1]);
        curNode.left && queue.push([curNode.left, level+1]);
    }
    return ans
};