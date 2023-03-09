/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left = 0;
    let right = height.length - 1;
    let max = 0;
    let cur = 0;
    
    while(left < right){
        let low = Math.min(height[left], height[right]);
        cur = low * (right-left);
        max = Math.max(cur, max);
        
        if(height[left] < height[right]) left++;
        else right--;
    }
    return max
};