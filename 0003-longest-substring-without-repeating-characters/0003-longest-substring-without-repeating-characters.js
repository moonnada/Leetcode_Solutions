/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    /*
    1. init a set
    2. init a end and max as 0
    3. traverse the input string to get longest
        3-1) while set has the cur char, delete the char in the set, and left is incremented
        3-2) set has not the cur char, put the char in the set and get max
    */
    
    let set = new Set();
    let max = 0;
    let left = 0;
    for(let i=0; i<s.length; i++){
        while(set.has(s.charAt(i))){
            set.delete(s.charAt(left))
            left+= 1;
        } 
        set.add(s.charAt(i));
        max = Math.max(max, i-left + 1);
    }
    return max
};