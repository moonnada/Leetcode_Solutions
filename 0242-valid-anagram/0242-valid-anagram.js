/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
   /*
    U)
    q) input str can have any char? even empty space?
    
    M) sort
    P) 
    1. check edge cases (if both strs length are different, then return false)
    2. sort alphabetically both strs
    3. init a map
    4. traverse sorted 's' str to put key and val
    5. traverse sorted 't' str and if any cnt is different, then return false
    6. out of loop, return true
    */
    
    if(s.length !== t.length) return false;
    
    let map = new Map();
    for(let i=0; i<s.length; i++){
        map[s[i]] = map[s[i]] ? map[s[i]] + 1 : 1;
    }
    
    for(let i=0; i<t.length; i++){
        if(!map[t[i]]) return false
        map[t[i]]--;
    } return true
}