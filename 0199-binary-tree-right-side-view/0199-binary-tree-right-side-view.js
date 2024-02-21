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
    //bfs
//     if(!root) return [];
//     let queue = [[root, 0]];
//     let ans = [];
    
//     while(queue.length){
//         let [curNode, level] = queue.shift();
//         if(ans.length === level) ans.push(curNode.val);
        
//         curNode.right && queue.push([curNode.right, level+1])
//         curNode.left && queue.push([curNode.left, level+1])
//     }
//     return ans
    
    //dfs
    if(!root) return [];
    let ans = [];
    pre(root, 0);
    return ans;
    
    function pre(node, level){
        if(!node) return;
        
        ans[level] = node.val;
        pre(node.left, level+1)
        pre(node.right, level+1)
    }
};