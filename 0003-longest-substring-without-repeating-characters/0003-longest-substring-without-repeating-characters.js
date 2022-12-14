/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    /*
    sliding windows. Time: O(n), Space: O(n)
    1. init a map(key: curElement, val: curIndex)
    2. init basic vals(maxLen, start)
    3. traverse the input string from 0 to the end
        3-1) if map has curElement, then update start
        3-2) update map with curElement and index
        3-3) get maxLen
    4. return maxLen
    */
    
    let map = new Map();
    let start=0, maxLen=0;
    for(let end=0; end<s.length; end++){
        if(map.has(s[end])){
            //if the cur char was seen, move the start to (1 + the last index of this char )
            //max prevents moving backward, 'start' can only move forward
            start = Math.max( map.get(s[end])+1, start)
        }
        map.set(s[end], end);
        maxLen = Math.max(maxLen, end-start+1)
    }
    return maxLen
   
   
}