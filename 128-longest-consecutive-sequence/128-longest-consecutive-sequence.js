/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    /*
    Method: hashset, time: o(n), space: o(n)
    1. save input array as a set
    2. count consecutive numbers within the set by keep adding 1 and record max
    3. only check numbers that is the smallest in a consecutive(!set.has(n-1)).
    */
    
    let set = new Set(nums);
    let cnt = 0;
    let max = 0;
    for(let n of set){
        if(!set.has(n-1)){
            cnt = 0;
            while(set.has(n)){
                n++;
                cnt++;
                max = Math.max(cnt, max);
            }
        }
    } return max    
};