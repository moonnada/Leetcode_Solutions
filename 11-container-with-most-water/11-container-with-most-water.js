/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
   /*
   two pointer
    0 1 2 3 4 5 6 7 8
   [1,8,6,2,5,4,8,3,7]
   
   1. init two pointers(left and right) and result
   2. while left < right, get min val between left and right
   3. get area = (right - left) * min
   4. compare cur result and area to get max value between them
   5. if arr[left] < arr[right] left++, else right--
   */
    let left = 0;
    let right = height.length-1;
    let ans = 0;
    while(left< right){
        let small = Math.min(height[left], height[right])
        let area = (right-left) * small
        ans = Math.max(area, ans);
        
        if(height[left] < height[right]) left++;
        else right--;
    }
    return ans
};