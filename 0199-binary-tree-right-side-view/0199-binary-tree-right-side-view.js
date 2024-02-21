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
    /*
    1.init a queue [node, level]
    2. check edge case(empty)
    3. init an ans arr
    4. while queue exists,
        4.1) check the cur node and its level from queue
        4.2) if ans.length = cur level, then put the cur val into the ans arr
        4.3) if curval has the right child, then put the val into queue
        4.4) if curval has the left child, put the val into que
    5. return ans
    */
    if(!root) return [];
    let queue = [[root, 0]];
    let ans = [];
    
    while(queue.length){
        let [curNode, level] = queue.shift();
        if(ans.length === level) ans.push(curNode.val)
        
        if(curNode.right) queue.push([curNode.right, level+1])
        if(curNode.left) queue.push([curNode.left, level+1])
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