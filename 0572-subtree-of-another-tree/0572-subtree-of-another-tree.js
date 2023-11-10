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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function(root, subRoot) {
    /*
    dfs
    */
   
    if(!root) return false;
    if(areSame(root, subRoot) || !subRoot) return true;
    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    
    function areSame(t1,t2){
        if(!t1 && !t2) return true;
        if(!t1 || !t2) return false;
        if(t1.val === t2.val) {
            return areSame(t1.left, t2.left) && areSame(t1.right, t2.right)
        }
    }
};