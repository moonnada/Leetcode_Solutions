/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    let set = new Set(nums);
    let max = 0;
    for(let n of set){
        if(!set.has(n-1)){
            let cnt = 0;
            while(set.has(n++)){
                cnt++;
            }
            max = Math.max(cnt, max)
        }
    }
    return max
};