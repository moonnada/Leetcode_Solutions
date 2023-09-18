/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    let left =0;
    let right = 0; 
    let max = 0;
    let map = new Map();
    
    while(right < s.length){
        map.set(s[right], (map.get(s[right]) || 0) +1);
        
        max = Math.max(max, map.get(s[right]));
        if(right-left+1 - max > k){
            map.set(s[left], map.get(s[left])-1);
            left++;
        } right++;
    }
    return right - left
};