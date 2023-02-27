/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    /*
    hashmap
    1. init a map
    2. during traversing the input arr using a loop, 
        init a looking val as target - nums element
        if map has a looking val, return as arr like [ map.get(looking val) , cur indice]
        else map.set ( num[indice] , 1)
    */

    let map = new Map();
    for(let i=0; i<nums.length; i++){
        let lookFor = target - nums[i];
        if(map.has(lookFor)) return [ map.get(lookFor), i];
        else map.set(nums[i], i);
    }
    
};