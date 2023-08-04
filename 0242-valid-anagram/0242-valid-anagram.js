/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    /*
    map
    
    1. init a map (key: char, value: cnt)
    2. chech edge cases
    3. iterative the s str to put key and value
    4. iterative the t str to compare each key and value. if find different, return false.
    5. return true
    */
    
    if(s.length !== t.length) return false;
    let table = new Array(26).fill(0);
    
    for(let i=0; i<s.length; i++){
        table[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
    }
    
    for(let i=0; i<t.length; i++){
        table[t.charCodeAt(i) - 'a'.charCodeAt(0)]--;
        if(table[t.charCodeAt(i) -'a'.charCodeAt(0)]  < 0) return false;
    }
    return true
};