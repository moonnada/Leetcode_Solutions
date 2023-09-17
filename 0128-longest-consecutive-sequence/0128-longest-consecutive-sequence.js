/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    /*
    run in o(n) time.
    
    1. init a set and put the input nums into the set
    2. traverse the set in find the consecutive numbers
        2.1) while (set.has(n-1)), cnt++. max = math.max(cnt, max)
    */
    
   let set = new Set(nums);
    let max = 0;
    for(let n of set){
        if(!set.has(n-1)){
            let cnt = 0;
            while(set.has(n)){
                cnt++;
                n++;
                max = Math.max(max, cnt)
            }
        }
    }
    return max
};