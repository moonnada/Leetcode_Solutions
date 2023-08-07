/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    /*
    Input: s = "AABABBB", k = 1

    left: 0
    right: 2
    
    if right - left +1 - max >k
        map[left]--;
        left++;
        
   map: [
   A: 2
   B:
   ]
    */
    let left = 0;
    let right = 0;
    let max = 0;
    let map = new Map();
    
    while(right < s.length){
        let curChar = s.charAt(right);
        map.set(curChar, (map.get(curChar) || 0) + 1)
        
        max = Math.max(max, map.get(curChar));
        
        if(right-left+1-max > k){
            map.set(s.charAt(left), map.get(s.charAt(left)) -1)
            left++;
        } right++;
    }
    return right-left;
};