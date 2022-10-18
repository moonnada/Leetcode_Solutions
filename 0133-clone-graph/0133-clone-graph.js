/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function(node) {
    /*
    1. check edge cases(empty, one node)
    */
    let start = node;
    if(start === null || start.length === 1) return null;
    let map = new Map();
    
    let queue = [start];
    map.set(start, new Node(start.val));
    
    while(queue.length > 0){
        let curVal = queue.shift();
        for(let neighbor of curVal.neighbors){
            if(!map.has(neighbor)){
                map.set(neighbor, new Node(neighbor.val));
                queue.push(neighbor);
            }
            map.get(curVal).neighbors.push(map.get(neighbor));
        }
    }
    
    return map.get(start)
};