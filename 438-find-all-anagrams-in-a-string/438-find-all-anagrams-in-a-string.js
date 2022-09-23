/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    if(s.length < p.length) return [];
    let needed = {};
    for(let i=0; i<p.length; i++){
        needed[p[i]] = ( needed[p[i]] || 0) + 1;
    }
    
    let left = 0, right = 0, requiredLength = p.length;
    let ans = [];
    while(right < s.length){
        if(needed[s[right]] > 0){
            requiredLength--;
        }
        needed[s[right]]--;
        right++;
        
        if(requiredLength === 0){
            ans.push(left);
            
        }
        
        if(right - left === p.length){
            if(needed[s[left]] >= 0){
                requiredLength++;
            }
            needed[s[left]]++;
            left++;
        }
    }
    return ans
};