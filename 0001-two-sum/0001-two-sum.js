/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    /*
        U:
        q) negative num could be a nums val?
        
        M: map => key as indice, val as element
        P: 
            1. init a map
            2. traverse the input arr and 
                if map has target - curVal, return curIndice and map's indice
                else put indice and num into map
    */
    let map = new Map();
    for(let i=0; i<nums.length; i++){
        if(map.has( target - nums[i])) return [ map.get(target-nums[i]) , i];
        map.set(nums[i] , i);
    }
};