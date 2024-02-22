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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    //bfs
    if(!root) return [];
    let queue = [root];
    let ans = [];
    
    while(queue.length){
        let curLevel = [];
        let queLevel = queue.length;
        for(let i=0; i<queLevel; i++){
            let curNode = queue.shift();
            if(curNode.left) queue.push(curNode.left);
            if(curNode.right) queue.push(curNode.right);
            
            curLevel.push(curNode.val)
        }
        ans.push(curLevel)
    }
    return ans
    
};