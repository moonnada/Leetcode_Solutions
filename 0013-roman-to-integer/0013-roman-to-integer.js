/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    /*
    4 or 9
    IV , IX
    
    14 19
    
    Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

IXXCCM


    */
    
    const symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    value = 0;
    for(let i = 0; i < s.length-1; i+=1){
        symbols[s[i]] < symbols[s[i+1]] ? value -= symbols[s[i]]: value += symbols[s[i]]
    }
    return value + symbols[s[s.length-1]];
};