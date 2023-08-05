/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
//     let leftArr = [];
//     let rightArr = [];
//     let leftMulti = 1;
//     let rightMulti = 1;
    
//     for(let i=0; i<nums.length; i++){
//         leftArr[i] = leftMulti;
//         leftMulti *= nums[i];
//     }
    
//     for(let i=nums.length-1; i>=0; i--){
//         rightArr[i] = rightMulti;
//         rightMulti *= nums[i];
//         rightArr[i] *= leftArr[i]
//     }
//     return rightArr;
    
    let ans = [];
    let multi = 1;
    
    for(let i=0; i<nums.length; i++){
        ans[i] = multi;
        multi *= nums[i];
    }
    
    multi = 1;
    for(let i=nums.length-1; i>=0; i--){
        ans[i] *= multi;
        multi *= nums[i];
        
    }
    return ans;
};