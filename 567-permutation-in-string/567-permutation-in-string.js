/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    /*
    sliding window
    1. edge cases
    2. init an object to store the frequency of s1's char
    3. init a left and right pointer, requiredLength
    4. iterate a loop to put s1's char and frequency into the object
    5. while right < s2.length, if find a s1's char in s2's index, then decrement the requiredLength
    6. since we have encountered new char, s2[right] is decremented and increment to the right side
    7. if requiredLength = 0, return true
    8. if right - left = s1.length => this means length is same, but have different val. then we have to remove left element of window.
    9. end of loop, return false
    */
    if (s1.length > s2.length) return false;
    let needed = {};
    for(let i=0; i<s1.length; i++){
        needed[s1[i]] = ( needed[s1[i]] || 0)+1
    }
    
    let left =0, right=0, requiredLength = s1.length;
    
    while(right < s2.length){
        if(needed[s2[right]] > 0){
           requiredLength--;
        }
        
        needed[s2[right]]--;
        right++;
        if(requiredLength === 0) return true;
        
        if(right - left === s1.length){
           if(needed[s2[left]] >= 0) {
               requiredLength++;
           }
            needed[s2[left]]++;
            left++;
        }
    }
    return false
}