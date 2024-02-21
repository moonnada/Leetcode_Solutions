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
    1. check edge cases(empty, one node)
    2. init a queue with the root noode
    3. while queue exists
        3.1) pop the cur val
        3.2) if cur val's left exist, put the val into queue
        3.3) else if cur val's right exists, put th
    */
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
            
            curLevel.push(cur.val)
        }
        ans.push(curLevel)
    }
    return ans
};