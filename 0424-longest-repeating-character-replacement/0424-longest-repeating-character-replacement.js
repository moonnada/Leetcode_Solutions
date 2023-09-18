/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    /*
    s = "AABABBA", k = 1
    
    => ans = 4
    
    sliding window 
    */
 
    let left = 0;
    let right = 0;
    let map = new Map();
    let max = 0;
    
    while(right < s.length){
        let curChar = s[right];
        map.set(curChar, (map.get(curChar) || 0) + 1 );
        
        max = Math.max(map.get(curChar), max)
        
        if(right-left+1 - max > k){
            map.set(s[left], map.get(s[left]) -1);
            left++;
        }  right ++;
        
    } return right - left
}