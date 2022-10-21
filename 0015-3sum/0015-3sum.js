/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
  /*
  two pointers
  1. sort the input arr
  2. iterate the sorted arr. start from 0 to arr.length-2. the reason visting till length-2 is one of pointers will be assigned for the last num
  3. check whether there is dulpicate num constantly. if is, continue;
  4. init two ptrs(mid, end)
  5. while mid < end, if sum of the three position values are eaqule to 0, then push to the ans arr. 
    6. first of all, check there is duplicate num constantly on mid and end position
    7. mid is incremented and end is decremented 
  
  */
    
    nums = nums.sort((a,b) => a-b);
    let ans =[];
    for(let i=0; i<nums.length-2; i++){
        if(nums[i] > 0) break;
        if(i>0 && nums[i] === nums[i-1]) continue;
        
        let mid = i+1;
        let end = nums.length-1;
        
        while(mid < end){
            let sum = nums[i] + nums[mid] + nums[end];
            if( sum === 0){
                ans.push([nums[i], nums[mid], nums[end]]);
                 
                while(nums[mid] === nums[mid+1]) mid++;
                while(nums[end] === nums[end-1]) end--;
            
                mid++; 
                end--;
            }else {
                sum > 0 ? end-- : mid++;
            }
            
           
        }
    }
    return ans;
}