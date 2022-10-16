/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
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
    function dfs(idx, cur){
        if(idx === digits.length){
            return ans.push(cur)
        }
        
        let letters = map[digits[idx]]
        for(let char of letters){
            console.log(cur);
            dfs(idx+1, cur+char)
        }
    }
    
    dfs(0,[]);
    return ans;
};