/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    /*
    sliding window with map
    1. init a map (key, val) => (cur element, index)
    2. init start and max val
    3. traverse the input string
    3-1) if map has cur element, that means there are duplicate char already in map, move the start to 1 + the last index of the char. max prevents moving backward. start can only move forward.
    3-2) put cur element and index into map
    3-3) get maxLength 
    */
    
    let map = new Map();
    let maxLen = 0;
    let start = 0;
    for(let end =0; end<s.length; end++){
        if(map.has(s[end])){
            start = Math.max(map.get(s[end])+1 , start);
        }
        map.set(s[end], end);
        maxLen = Math.max(end-start+1, maxLen);
    }
    return maxLen
    
};