/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
  /*
  two ptrs
  1. init two prts(left, right)
  2. while( left < right), find the low val between height[left] and height[right]
    3. get area = (right-left) * low val 
    4. get maxArea = math.max(area, maxArea)
    
    if(height[left] < height[right]) right--, else left++
  */
    
    let left = 0;
    let right = height.length-1;
    let maxArea = 0;
    while(left < right){
        let low = Math.min(height[left], height[right]);
        let area = (right-left)*low;
         maxArea = Math.max(area, maxArea);
        
        if(height[left] < height[right]) left++;
        else right--
    } return maxArea
};