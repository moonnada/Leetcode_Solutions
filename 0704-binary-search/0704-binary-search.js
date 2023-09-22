/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
  
    let mid = Math.floor(nums.length /2)
    
    
     if(nums[mid] < target){
        for(let i=mid; i<nums.length; i++ ){
            if(nums[i] === target) return i;  
        }
    } else {
        for(let i=0; i<=mid; i++){
            if(nums[i] === target) return i;
        }
    } return -1
    
    
};