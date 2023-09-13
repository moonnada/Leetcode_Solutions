/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    /*
              0 1 2 3 4 5 6 7 8
    height = [1,8,6,2,5,4,8,3,7]
              L               R
    get width and height 
    
    */
    let left = 0;
    let right = height.length-1;
    let max = 0;
    while(left < right){
        let width = right - left;
        let validHeight = Math.min(height[left], height[right]);
        if(height[left] >= height[right]){
            right--;
        }else {
            left++;
        }
        max = Math.max(max, width*validHeight);
        
    }
    return max
};