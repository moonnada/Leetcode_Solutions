/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    /*
    time : O(n) , space: O(n)
    ex) nums = [1,2,3,4] => [24,12,8,6]
        left = [1,(1)x1 , (1x1)x2 , (1x1x2)x3] = [1,1,2,6]
        right = [ (1x4x3)x2  , (1x4)x3 ,(1)x4,1] = [24, 12, 4, 1]
        left*right = [24,12,8,6]
        
    1. init two empty arrays for left and right sides
    1.1) 1 array with increment multiplication from left, 1 array with increment multiplication from right
    2. at the start index of these arrays, we will use 1
    3. get multiplication on each side
    4. multiply left and right
    */
    
//     let left = [];
//     let right = [];
//     let leftMulti = 1;
//     let rightMulti = 1;
    
//     for(let i=0; i<nums.length; i++){
//         left[i] = leftMulti;
//         leftMulti *= nums[i];
//     }
    
//     for(let i=nums.length-1; i>=0; i--){
//         right[i] = rightMulti;
//         rightMulti *= nums[i];
//         right[i] *= left[i]
//     }
//     return right
    
    
    //optimisation
    //time: o(n), space :o(1)
    if (nums === null || nums.length <= 1) {
        return [];
    }
    let ans = [];
    let leftMulti = 1;
    let rightMulti = 1;
    
    for(let i=0; i<nums.length; i++){
        ans[i] = leftMulti;
        leftMulti *= nums[i]
    }
    
    for(let i=nums.length-1; i>=0; i--){
        ans[i] *= rightMulti;
        rightMulti *= nums[i];
    }
    return ans;
};