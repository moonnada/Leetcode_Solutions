/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s.length !== t.length) return false;
    let map = {};
    for(let i=0; i<s.length; i++){
        map[s[i]] = map[s[i]] ? map[s[i]] + 1 : 1;
    }
    
    for(let i=0; i<t.length; i++){
        if(!map[t[i]]) return false;
        map[t[i]]--;
    }
    return true
}