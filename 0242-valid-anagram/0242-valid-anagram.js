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
//     let map = {};
    
//     for(let char of s){
//         map[char] = (map[char] || 0) + 1;
//     }
    
//     for(let char of t){
//         if(!map[char]) return false
//         map[char]--;
//     }
    let map = new Map();
    for(let i=0; i<s.length; i++){
        map.set(s[i], (map.get(s[i]) || 0)+1 )
    }
    
    for(let i=0; i<t.length; i++){
        if(!map.has(t[i]) || map.get(t[i]) == 0) return false;
        map.set(t[i], map.get(t[i])-1)
    }
    return true
};