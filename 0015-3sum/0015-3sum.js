/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    /*
            nums = [-1,0,1,2,-1,-4]
    sort [-4,-1,-1,0,1,2]
    
    1. sort the input arr
    2. traverse the arr from 0 to len -2
        2.0) check edge cases to avoid duplication
        2.1) init two pointers
    */
    
    nums.sort((a,b) => a-b);
    let ans = [];
    for(let i=0; i<nums.length-2; i++){
        if(i>0 && nums[i] === nums[i-1]) continue;
        
        let mid = i+1;
        let end = nums.length-1;
        
        while(mid < end){
            let sum = nums[i] + nums[mid] + nums[end];
            if(sum === 0 ){
                ans.push([nums[i], nums[mid], nums[end]])
                
                while(nums[mid] === nums[mid+1]) mid++;
                while(nums[end] === nums[end-1]) end--;
                
                mid++;
                end--;
            } else {
                sum > 0 ? end-- : mid++;
            }
        }
    }
    return ans
};