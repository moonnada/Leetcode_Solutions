/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
   /*
   U:
   q) if input arrary is empty, what do i need to return
   
   M: map (key: num, val: cnt)
   P: 
   1. init a map
   2. traverse the input arr and if map has a same val, then return true. if not put key and val into the map
   3. out of loop, return false
   
   
    */
    let map = new Map();
    for(let i=0; i<nums.length; i++){
         if (map.has(nums[i]) )return true;
        map.set(nums[i])
    } return false
}