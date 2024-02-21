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
    if(!root) return [];
    let queue = [[root, 0]];
    let ans = [];
    
    while(queue.length){
        let [curVal, curLevel] = queue.shift();
        
        if(ans.length === curLevel){
            ans.push(curVal.val)
        }
        
        curVal.right && queue.push([curVal.right, curLevel+1])
        curVal.left && queue.push([curVal.left, curLevel+1])
    }
    return ans
    //dfs
//     if(!root) return [];
//     let ans = [];
//     pre(root, 0);
//     return ans;
    
//     function pre(node, level){
//         if(!node) return;
        
//         ans[level] = node.val;
        
//         pre(node.left, level+1);
//         pre(node.right, level+1)
//     }
};