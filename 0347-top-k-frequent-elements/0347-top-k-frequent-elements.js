/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    /*
    U: 
    q) can input arr be empty or have negqtive numbers?
    
    1: 3
    2: 2
    3: 1
    
    M:
    hashmap (key: element, val: cnt)
    bucket sort
   */
    
    let map = new Map();
    let bucket = [];
    let ans = [];
    
    for( num of nums){
        map.set( num, (map.get(num) || 0) + 1 )
    }
    
    for(let [num, freq] of map){
        bucket[freq] = (bucket[freq] || new Set()).add(num)
    }
    
    for(let i=bucket.length-1; i>=0; i--){
        if(bucket[i]) ans.push(...bucket[i])
        if(ans.length === k) break
    }
    return ans
};