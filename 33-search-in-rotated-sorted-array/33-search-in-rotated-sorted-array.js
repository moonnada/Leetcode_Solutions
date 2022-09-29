/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    /*
    binary
   
    */
    
//     let start = 0, end = nums.length-1;
//     while(start <= end){
//         let mid = Math.floor((start + end) /2 );
//         if(target === nums[mid]) return mid;
        
//         if(nums[start] <= nums[mid]){
//             if(nums[start] <= target && target <= nums[end]){
//                 end = mid -1;
//             } else {
//                 start = mid + 1
//             }
//         } 
//         else {
//             if( nums[mid] <= target && target <= nums[end]){
//                 start = mid +1;
//             } else {
//                 end = mid -1;
//             }
//         }
//     }
     let left = 0;
  let right = nums.length - 1;
    
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    
    if (nums[mid] === target) {
      return mid;
    }
    
    // When dividing the roated array into two halves, one must be sorted.
    
    // Check if the left side is sorted
    if (nums[left] <= nums[mid]) {
      if (nums[left] <= target && target <= nums[mid]) {
        // target is in the left
        right = mid - 1;
        
      } else {
        // target is in the right
        left = mid + 1;
      }
    } 
    
    // Otherwise, the right side is sorted
    else {
      if (nums[mid] <= target && target <= nums[right]) {
        // target is in the right
        left = mid + 1;

      } else {
        // target is in the left
        right = mid - 1;
      }
    }
    
    
  }
    
    return -1
};