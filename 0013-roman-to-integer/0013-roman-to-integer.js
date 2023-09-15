/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
   /*
   I C   D
   1 100 500
   */
    const syn = {
        'I' : 1,
        'V' : 5,
'X' :10,
'L'  :50,
'C'            :100,
'D'             :500,
'M'             :1000
    }
    
   let ans = 0;
    for(let i=0; i<s.length; i++){
        let cur = syn[s[i]];
        let next = syn[s[i+1]];
        
        if(cur < next){
            ans += next - cur;
            i++;
        } else {
            ans += cur
        }
    }
    
    return ans
};