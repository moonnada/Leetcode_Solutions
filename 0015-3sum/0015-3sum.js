/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    /*
    1. sort input arr
    2. init output arr
    3. traverse the sorted arr to find sum = 0
        3-1) if i > 0, then break
        3-2) if (i > 0 && curElement and curElement -1 are equal), then continue // to avoid getting the same format
        3-3) init mid and right val
        4. while (mid < right) init sum value
        5. if sum = 0, put cur three elements into arr
            6. to check there is the same element constantly for mid and right 
            7. mid++, right--;
        8. else sum > target ? right-- : mid++
        
    */
    
  
    nums.sort((a,b) => a-b);
    let ans = [];
    
    for(let i=0; i<nums.length-2; i++){
        if(i>0 && nums[i] === nums[i-1]) continue;
        
        let mid = i+1;
        let end = nums.length-1;
        
        while(mid < end){
            
            let sum = nums[i] + nums[mid] + nums[end];
            if(sum === 0) {
                ans.push([ nums[i], nums[mid], nums[end]])
            
                while(nums[mid] === nums[mid+1]) mid++;
                while(nums[end] === nums[end-1]) end--;
            
                  mid++; end--;
            } else{
             sum > 0 ? end-- : mid++;

            }
        }
       
    }
     return ans;
};