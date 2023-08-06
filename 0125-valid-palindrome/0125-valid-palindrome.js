/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    /*
    - remove non-alphabenumric. only contain number and lowercase.
    - empty str => true
    
    1. check edge cases(null, one length)
    2. init two ptrs(left and right)
    3. convert the input str to contain numbers and lowercases only
    4. while left <= right
        3.1) if left element and right element are same, left++, right--
        3.2) else return false
    5. return true
    */
    
    if(s.length === 0 || s.length ===1) return true;
    s = s.toLowerCase();
    s = s.replace(/[^A-Za-z0-9]/g, '');
    let left = 0;
    let right = s.length-1;
    while(left <= right){
        if(s.charAt(left) === s.charAt(right)){
            left++;
            right--;
        } else {
            return false;
        }
    }
    return true
}