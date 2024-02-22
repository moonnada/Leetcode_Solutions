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
    /*
    1. check edge case
    2. init a queue and ans array
    3. while queue exists
        3.1) init a curLevel array 
        3.2) init a cur queue length 
        3.3) make a loop to traverse each side. in a loop, get a cur node from queue and put each side into curLevel arr if exist
        3.4) put tue curLevel arr into ans arr
    
    */
    
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