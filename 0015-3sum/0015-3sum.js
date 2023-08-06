/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    /*
    - three indexs are all distinct
    - return order doesnt matter
    
    ex) nums = [-1,0,1,2,-1,-4]
        output = [[-1,0,1] , [-1,2,-1]]
        
    1. sort input arr
    2. init an output arr
    3. traverse the sorted arr to find 3 sum
        3.1) if i>0 and nums[i] = nums[i-1], keep going through
        3.2) init a mid and end points
        3.3) while mid < end
            3.3.1) if cur three points val are equal to 0, then add to ans
                3.3.2) check mid and end points are same continuesly. 
                3.3.3) mid and end ptrs are moving
            3.4) else sum > 0 ? end-- : mid++
    */
    
    nums.sort((a,b) => a-b);
    let ans = [];
    for(let i=0; i<nums.length-2; i++){
        if(i>0 && nums[i] == nums[i-1]) continue;
        
        let mid = i+1;
        let end = nums.length-1;
        
        while(mid < end){
            let sum = nums[i] + nums[mid] + nums[end];
            if( sum == 0){
                ans.push([nums[i],nums[mid],nums[end]]);
                
                while(nums[mid] == nums[mid+1]) mid++;
                while(nums[end] == nums[end-1]) end--;
                
                mid++;
                end--;
            } else {
                sum > 0 ? end-- : mid++;
            }
            
        }
    }
    return ans
    
};