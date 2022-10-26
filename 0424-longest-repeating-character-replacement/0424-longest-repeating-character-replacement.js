/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    /*
    using slide window. left and right
    */
   
    let left=0, right=0, maxCharCnt = 0;
    const visited = {};
    
    while(right < s.length){
        const char = s[right];
        visited[char] = visited[char] ? visited[char]+1 : 1;
        
        maxCharCnt = Math.max(maxCharCnt, visited[char]);
        
        if(right-left+1 - maxCharCnt > k){
            visited[s[left]]--;
            left++;
        }
        right++;
    }
    return right-left
};