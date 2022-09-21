/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
   // keeps track of the most recent index of each letter.
    const seen = new Map();
    // keeps track of the starting index of the current substring.
    let start = 0;
    // keeps track of the maximum substring length.
    let maxLen = 0;
    
    for(let end = 0; end < s.length; end++) {
        // if the current char was seen, move the start to (1 + the last index of this char)
        // max prevents moving backward, 'start' can only move forward
        if(seen.has(s[end])) {
            start = Math.max(seen.get(s[end]) + 1, start)
        }
        seen.set(s[end], end);
        // maximum of the current substring length and maxLen
        maxLen = Math.max(end - start + 1, maxLen);
    } 
    
    return maxLen;  
};