/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    /*
    hashmap
    1. init a hashmap
    2. traver the input arr and put every element into map
    3. if( map has target - cur elemnt) return map
    */
    // let map = new Map();
    // for(let i=0; i<nums.length; i++){
    //     if(map.has(target - nums[i])){
    //         return [map.get(target - nums[i]), i];
    //     } map.set(nums[i], i)
    // }
    
    //two pointer
    // for(let start=0, end=nums.length-1; start<end; ) {
    //     let sum = nums[start] + nums[end];
    //     if(sum === target){
    //         return [start++, end++]
    //     } 
    //     else sum > target ? end-- : start++
    // }
    
   let map = new Map();
    for(let i=0; i<nums.length; i++){
        if(map.has(target - nums[i])){
            return [ map.get(target - nums[i]) , i]
        } else {
            map.set(nums[i], i)
        }
    }
    
   
     
};