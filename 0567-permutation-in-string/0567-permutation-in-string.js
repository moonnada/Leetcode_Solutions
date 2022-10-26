/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    /*
 sliding window
 1. edge cases
 2. init an object to store s1's char
 3. iterative a loop to put s1's char into object
 4. init left and right ptrs
 5. while right < s2.length
    6. if s2's char is in object, then decrease requiredlength
    7. 
    7. if requiredlength = 0, return true;
    8. 
  */
    if(s1.length > s2.length) return false;
    let needed = {};
    for(let i=0; i<s1.length; i++){
        needed[s1[i]] = needed[s1[i]] ? needed[s1[i]]+ 1 : 1
    };
    
    let left=0, right=0, requiredLength = s1.length;
    
    while(right < s2.length){
        if(needed[s2[right]] > 0) requiredLength--;
        
        needed[s2[right]]--;
        right++;
        
        if(requiredLength === 0) return true;
        
        if(right-left === s1.length){
            if(needed[s2[left]] >=0) requiredLength++;
            needed[s2[left]]++;
            left++;
        }
    } return false
}