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
 
    if(s.length === 0 ) return true;
    
    const lowercases = s.toLowerCase();
    const removeSpaces = lowercases.split(" ").join("");
    const onlyAlphabets = removeSpaces.replace(/[^a-zA-Z0-9 ]/g, '');
    
    let left = 0;
    let right = onlyAlphabets.length-1;
    while(left <= right){
        console.log(onlyAlphabets[left])
        console.log(onlyAlphabets[right])
        if(onlyAlphabets[left] !== onlyAlphabets[right]) return false;
        left++;
        right--
    } return true
}