/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  /*
  q1. input arr has any integer nums? even negative num?
  q2. what if target is 0, and input arr has 0 elements
  
  m : hashmap (key: array's element, val: each element's count)
  
  1. init a hashamp
  2. traverse the input arr and initialize lookingval. 
  3.    if map has the lookingVal, then just return the curIndice and lookingVal's element
  4.    else map.set(lookingVal and indice)
  */

    let map = new Map();
    for(let i=0; i<nums.length; i++){
        let lookFor = target - nums[i];
        if(map.has(lookFor)){
            return [ map.get(lookFor), i];
        }
        map.set(nums[i], i);
    }
  
    
};