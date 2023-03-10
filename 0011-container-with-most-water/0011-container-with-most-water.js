/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left = 0;
    let right = height.length - 1;
    let max = 0;
    let min = 0;
    let cur = 0;
    
    while(left < right){
        min = Math.min(height[left], height[right]);
        cur = (right-left) * min;
        max = Math.max(cur, max);
        
        height[left] < height[right] ? left++ : right--;
        
    }
    return max
};