/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
   let temp = []
    let result = []

    function backtracking(temp, nums) {
      if(nums.length == 0) {
          result.push([...temp])
          return
       }
    
      for(let i=0; i<nums.length; i++) {
          temp.push(nums[i])
          nums.splice(i, 1)
          backtracking(temp, nums)
          nums.splice(i, 0, temp.pop())
       }
    }
    backtracking(temp, nums)
    return result
   
};