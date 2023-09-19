/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
  /*
   s1 = "ab", s2 = "eidbaooo"
   
   => need "ab" or "ba"
   1. if s1.length > s2.length, return false
   
  */
    
    if(s1.length > s2.length) return false;
    let map = new Map();
    
    for(let i=0; i<s1.length; i++){
        map.set(s1[i], (map.get(s1[i]) || 0) +1);
    }
    
    let left = 0;
    let right = 0;
    let requiredLen = s1.length;
    
    while( right < s2.length){
        if(map.get(s2[right]) > 0){
            requiredLen--;
        }
        
        if(requiredLen === 0) return true;
        
        map.set(s2[right], (map.get(s2[right]) || 0) -1)
        right++;
        
        if(right-left === s1.length){
            if(map.get(s2[left]) >= 0){
                requiredLen++;
            }
            
            map.set(s2[left], (map.get(s2[left]) || 0) +1)
            left++
        }
    }
    
    return false

};