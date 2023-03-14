/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
   let left = 0, right = 0, max = 0;
    let map = new Map();
    
    while(right < s.length){
        let curChar = s[right];
        map[curChar] = map[curChar] + 1 || 1;
        
        max = Math.max(max, map[curChar]);
        
        if(right - left + 1 - max > k) {
            map[s[left]]--;
            left++;
        } right++;
        
    }
    return right-left
};