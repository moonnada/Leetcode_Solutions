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
 * @return {boolean}
 */
var isValidBST = function(root) {
    /*
    1. check edge cases(empty)
    2. init a queue
    3. while queue exists
        3.1) get the cur val from queue
        3.2) if the cur val has left child, check less than the curval. if isnt return false, else put into que
        3.3)elif the cur val has right child, check greater than the curval. if isnt return false, else put into que
    4. return true  
    
    */
    //bfs
//     if(!root) return false
//     let queue = [[root, -Infinity, Infinity]];
    
//     while(queue.length){
//         let [curNode, minVal, maxVal] = queue.shift();
        
//         if(!curNode) continue;
//         if(curNode.val >= maxVal || curNode.val <= minVal) return false
        
//         queue.push([curNode.left, minVal, curNode.val])
//         queue.push([curNode.right, curNode.val, maxVal])
//     }
//     return true
   
    if(!root) return false;
    if(root.length === 1) return true;
    
    return helper(root, -Infinity, Infinity)
    
    function helper(node, lower, upper){
        if(!node) return true;
        if((lower < node.val) && (node.val < upper)){
            return helper(node.left, lower, node.val) && helper(node.right, node.val, upper)
        } return false
    }
    
};