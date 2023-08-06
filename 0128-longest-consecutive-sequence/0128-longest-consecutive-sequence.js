/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    /*
    U:
        - unsorted integer arr
        - return the len of the longest consecutive elements
        - must run in o(n) time
        q) input elements are all distinct?
        
    ex) nums = [100,4,200,1,3,2] 
    
    set: 100,4,200,1,3,2
    
    1. init a set which has input arr
    2. init a count and max as 0
    3. traverse the set to find consecutive elements
        3.1) if set not has n-1, cnt=0
        3.2) while set has n, cnt and n are incremented. get a new max
    4. return max
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
    }
    return max
    
};