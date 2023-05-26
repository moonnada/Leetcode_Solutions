/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let startLeft = 1;
    let startRight = 1;
    let ans = [];
    for(let i=0; i<nums.length; i++){
        ans[i] = startLeft;
        startLeft *= nums[i];
    }
    
    for(let i=nums.length-1; i>=0; i--){
        ans[i] *= startRight;
        startRight *= nums[i];
    }
    
    return ans
};