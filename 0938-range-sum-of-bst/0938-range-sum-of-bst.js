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
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var rangeSumBST = function(root, low, high) {
    /*
    U:
        q) root can be null?
    
    M: dfs (recursion)
    
    P: 
        1. check edge cases(null)
        2. init a new func to visit recursively
            
            2.1) if curnode.val >= low and curNode.val <= high, then add the val into the ans val
            2.2) if curNode.val > low, visit left
            2.2) if curNode.val < h, visit right
        3. return sum
    */
    
//     let sum = 0
//     const dfs = (node) => {
//         if(!node) return null
//         if(node.val >= low && node.val <= high) sum += node.val;
        
//         if(node.val > low && node.left !== null) dfs(node.left);
        
//         if(node.val < high && node.right !== null) dfs(node.right);
//     }
        
//     dfs(root)
    
    
//     return sum
    
    /*
    BFS - queue
    
    1. init a queue 
    2. while queue exists
        2.1) pop a node from queue
        2.2) if the node val >= low and node val <= high, add its val to sum
        2.3) if the node has a left child, put the node into queue
        2.4) if the node has a right child, put the node into queue
    3. return sum
    */
//     let sum = 0;
//     let queue = [root];
//     while(queue.length){
//         let node = queue.pop();
//         if(node.val >= low && node.val <= high){
//             sum += node.val;
//         }
//         if(node.left) queue.push(node.left);
//         if(node.right) queue.push(node.right);
//     }
    
//     return sum
    
    let sum = 0;
    let queue = [root];
    while(queue.length){
        let node = queue.pop();
        if(node.val >= low && node.val <= high) sum += node.val;
        if(node.left) queue.push(node.left);
        if(node.right) queue.push(node.right);
    }
    return sum;
}