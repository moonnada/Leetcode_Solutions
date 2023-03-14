/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    if(s1.length > s2.length) return false;
    let needed = {};
    for(let i=0; i<s1.length; i++){
        needed[s1[i]] = needed[s1[i]] ? needed[s1[i]]+ 1 : 1
    };
    
    let left=0, right=0, requiredLength = s1.length;
    
    while(right < s2.length){
        if(needed[s2[right]] > 0) {
            requiredLength--;
        }
        if(requiredLength === 0) return true;
        
        needed[s2[right]]--;
        right++;
        
        
        
        if(right-left === s1.length){
            if(needed[s2[left]] >=0) { 
                requiredLength++;
            }
            needed[s2[left]]++;
            left++;
        }
    } return false
};