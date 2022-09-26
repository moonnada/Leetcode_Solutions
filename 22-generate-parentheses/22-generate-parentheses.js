/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    let res = [];
    
    const dfs = (str, open, close) => {
        if(open < close) return;
        if(open === n && close === n){
            res.push(str); 
            return;
        }
        
        if(open < n) dfs(str + '(', open+1, close);
        if(close < n) dfs(str + ')', open, close+1);
    }
    dfs('', 0,0);
    return res;
};