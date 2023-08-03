/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    /*
    -key points
        1) 1<= s.length <=1000, and consists only lowercase letter.
        
        ex) e v e -> panlidrom
             
            L
            R
            
              v
        cnt:4
        
        
    P:
        1. traverse the input s
            1.1) init a left and right val
            1.2) check single char, using a helper func
            1.3) check even char,  using a helper func
        
        2. helper func,
            2.1) while check bounaries and current char is panlindrom, cnt++, left--, right++
            
        Time: O(n^2), space: o(1)
    */
    
    let cnt = 0;
    let left = 0;
    let right = 0;
    for(let i=0; i<s.length; i++){
        left = i;
        right = i;
        
        //check a single char
        helper(left, right);
        
        //check even chars
        helper(left, right+1);
    }
    
    function helper(left, right){
        while(left>=0 && right <= s.length-1 && s[left] == s[right]){
            cnt++;
            left--;
            right++;
        }
    }
    
    return cnt;
};