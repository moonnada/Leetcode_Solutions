/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    /*
    s = "anagram", t = "nagaram"
    
    1. compare both str length. if they are different, then return false
    
    */
   if(s.length !== t.length) return false;
    let map = {};
    
    for(let char of s){
        map[char] = (map[char] || 0) + 1;
    }
    
    for(let char of t){
        if(!map[char]) return false
        map[char]--;
    }
    
    return true
};