/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    /*
    ex)
     nums = [-1,0,1,2,-1,-4]
     
     1. sort.   nums = [-4,-1,-1,0,1,2]
     2. init an arr for answer
     3. init two pointer
    */
    
    nums.sort((a,b) => a-b);
    let ans = [];
    
    for(let i=0; i<nums.length-2; i++){
        if(i>0 && nums[i] === nums[i-1]) continue;
        
        let mid = i+1;
        let end = nums.length-1;
        
        while(mid < end){
            let sum = nums[i] + nums[mid] + nums[end];
            if(sum === 0){
                ans.push([nums[i], nums[mid], nums[end]]);
                
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