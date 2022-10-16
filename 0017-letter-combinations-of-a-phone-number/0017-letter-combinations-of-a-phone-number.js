/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    /*
    backtracking - dfs
    DFS approach as we will check each permutation of characters and store them in ans array.
    1. check edge cases(null, 0 length)
    2. store characters into nums
    3. in a dfs func, first of all, if curIndex is same as digits.length, then put curArray into ansArr. 
        After that, travese cur letters to find valid postion and idx 
    */
    if(digits == null || digits.length === 0 ) return [];
    const map = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz',
    }
    
    let ans = [];
    dfs([], 0);
    return ans;
    
    function dfs(cur, idx){
        if(idx === digits.length) return ans.push(cur);
        
        let letters = map[digits[idx]];
        
        for(let char of letters){
            dfs( cur+char, idx+1);
        }
    }
    
};