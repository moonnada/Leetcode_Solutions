/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    /*
    ex) s = "dvdfadbukh"
    
           i       c
    set: d,v,d,f,a,d
    len: 4
    max: 4
    
    P:
        1. check edge cases
        2. init a set and max val as 0
        3. traverse the input str to find the longest substr
            3.1) while set has the cur char in the set
                    left++, remove the char in the set\\
            3.2) put the char into set
            3.3) get the max len
    */
    
    let set = new Set();
    let max = 0;
    let left = 0;
    
    for(let i=0; i<s.length; i++){
        while(set.has(s.charAt(i))){
            set.delete(s.charAt(left));
            left++;
        } 
        set.add(s.charAt(i));
        max = Math.max(max, i-left+1);
    }
    return max
 
    
}
    
