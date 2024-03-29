/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
   if(!inorder || inorder.length <1) return null;
    let root = new TreeNode(preorder.shift());
    let index = inorder.indexOf(root.val);
    let leftTree = inorder.slice(0, index);
    let rightTree = inorder.slice(index + 1);
    
    root.left = buildTree(preorder, leftTree);
   root.right =  buildTree(preorder, rightTree);
    
    return root
};