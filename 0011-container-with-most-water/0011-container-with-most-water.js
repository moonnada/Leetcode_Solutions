/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    /*
    1. init two ptrs (left and right)
    2. while( left < right)
        2.1) get height. smaller one, then moving to the next
        2.2) get width
        2.3) get area
        2.4) get max area
        
    time: o(n), space: o(1)
    */
    
    let left = 0;
    let right = height.length-1;
    let area = 0;
    let max = 0;
    
    while(left < right){
        let width = right - left;
        let heightVal = Math.min(height[left], height[right]);
        area = width * heightVal;
        max = Math.max(max, area);
        if(height[left] < height[right]) left++;
        else right--;
    }
    return max;
    
    
    
};