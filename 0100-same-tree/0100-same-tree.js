/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    
    // if(!p && !q) return true;
    // else if(!p || !q ) return false;
    // else if(p.val !== q.val) return false;
    // return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    
    let queue = [[p,q]];
    while(queue.length){
        let [p,q] = queue.pop();
        if(!q && !p) return true;
        if(!p || !q) return false;
        if(p.val !== q.val ) return false;
        
        if(p.left || q.left) queue.push([p.left, q.left]);
        if(p.right || q.right) queue.push([p.right, q.right]);
    }
    return true
};