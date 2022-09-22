/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    /*
    using slide window. left and right
    */
    let left = 0, right = 0, max = 0, freq = 0;
    let arr = [];
    for(right = 0; right<s.length; right++){
        arr[s[right]] = arr[s[right]]+1 || 1;
        freq = Math.max(freq , arr[s[right]]);
        while(right-left+1 - freq > k){
            arr[s[left]]--;
            left++;
        }
        max = Math.max(max, right-left+1)
    }
    return max
};