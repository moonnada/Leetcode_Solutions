/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    /*
    binary
    1. init start and end val
    2. while start < end
    2-1) init a mid val
    2-2) if arr[mid] > arr[mid-1], end = mid-1
    2-3) else start = mid+1
    */
    let start = 0, end = nums.length-1;
   
    while(start < end){
        let mid = Math.floor((start + end) / 2);
        if(nums[mid] > nums[end]) start = mid +1;
        else end = mid
    }
    return nums[start]
};