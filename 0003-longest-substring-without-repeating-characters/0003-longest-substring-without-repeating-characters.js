/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    /*
    sliding windows
    1. init a map. (key: curElement, val: curindex)
    2. init values such as maxLen, start
    3. traverse the input string from 0 to the end 
        3-1) if map has curElement, then update start point as right next value to cur end point
        3-2) save Map with curelement and index
        3-3) update maxLen with using math.max
    4. return maxLen
    */
    
    let map = new Map();
    let maxLen = 0;
    let start = 0;
    
    for(let end=0; end<s.length; end++){
        if(map.has(s[end])){
           start = Math.max( map.get(s[end]) +1 , start);
        }
        map.set(s[end], end);
        maxLen = Math.max(end-start+1, maxLen)
    }
    return maxLen;
   
}