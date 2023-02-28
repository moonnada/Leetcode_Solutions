/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    /*
    HashMap (key: element, value: freq)
    bucket sort 
    ex) [1,1,1,2,2,3] => 
    freq: 0    1     2    3 
         [[], [3] , [2], [1] ]
         
    1. init a map
    2. put input arr into map depends on key and increment of freq
    3. put the map into bucket
    4. traverse the bucket from the last to the first element to put elements depends on freq
    */
    
    let map = new Map();
    let bucket = [];
    let ans = [];
    
    for(num of nums){
        map.set(num, (map.get(num) || 0) + 1)
    }
    
    for(let [num, freq] of map){
        bucket[freq] = (bucket[freq] || new Set()).add(num)
    }
    
    for(let i=bucket.length-1; i>=0; i--){
        if(bucket[i]) ans.push(...bucket[i]);
        if(ans.length === k) break;
    }
    return ans
    
    
};