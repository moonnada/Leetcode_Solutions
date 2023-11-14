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
    if(!root) return [];
    let queue = [root];
    let ans = [];
    
    while(queue.length){
        let queLevel = queue.length;
        let curLevel = [];
        for(let i=0; i<queLevel; i++){
            let cur = queue.shift();
            
            if(cur.left) queue.push(cur.left);
            if(cur.right) queue.push(cur.right);
            
            curLevel.push(cur.val);
        }
        ans.push(curLevel)
    }
    return ans
};