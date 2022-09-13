/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    /*
    U.
    ex.1) nums = [ 1,1,1,2,2,3], k =2 => [1,2]
    ex.2) nums = [ ] , k=2 => []
    ex.3) nums = [1,2,3] , k=3 => []
    q. is the input arr sorted?
    
    */
   let map = new Map();
    let bucket = [];
    let ans = [];
    
    for(let num of nums){
        map.set(num, (map.get(num) || 0) + 1);
    }
    
    for(let [num, freq] of map){
        bucket[freq] = (bucket[freq] || new Set()).add(num);
    }
    
    for(let i=bucket.length-1; i>=0; i--){
        if(bucket[i]) ans.push(...bucket[i])
        if(ans.length === k) break
    }
    return ans
};