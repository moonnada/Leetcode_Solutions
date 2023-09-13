/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let map = new Map();
    let bucket = [];
    let ans = [];
    
    for(let i=0; i<nums.length; i++){
        map.set(nums[i], (map.get(nums[i]) || 0) + 1 )
    }
    
    for(let [num, freq] of map){
        bucket[freq] = (bucket[freq] || new Set()).add(num)
    }
    
    for(let i=bucket.length-1; i>=0; i--){
        if(bucket[i]) ans.push(...bucket[i])
        if(ans.length === k) break;
    }
    return ans
};