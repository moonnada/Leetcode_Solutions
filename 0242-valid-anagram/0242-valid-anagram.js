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
    
    const map = {};
    
    for(let c of s){
        map[c] = (map[c] || 0) + 1;
    }
    
    for(let c of t){
        if(!map[c]) return false;
        map[c]--;
    } return true
};