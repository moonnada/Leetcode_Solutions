/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    /*
    s = "abcabcbb"
    
    */
    let set = new Set();
    let max = 0;
    let left = 0;
    for(let i=0; i<s.length; i++){
        while(set.has(s.charAt(i))){
            set.delete(s.charAt(left));
            left++;
        } 
        set.add(s.charAt(i))
        
         max = Math.max(max, i-left+1)
    }
    return max
   
};