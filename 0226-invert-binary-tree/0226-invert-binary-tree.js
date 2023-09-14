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
 * @return {TreeNode}
 */
var invertTree = function(root) {
  //dfs  
  // if(!root) return root;
  //   let left = invertTree(root.left);
  //   let right = invertTree(root.right);
  //   root.right = left;
  //   root.left = right;
  //   return root
    
    //bfs
    let queue = [root];
    if(!root) return root;
    while(queue.length){
        let curVal = queue.pop();
        let temp = curVal.left;
        curVal.left = curVal.right;
        curVal.right = temp;
        if(curVal.left) queue.push(curVal.left);
        if(curVal.right) queue.push(curVal.right)
    }
    return root
    
};