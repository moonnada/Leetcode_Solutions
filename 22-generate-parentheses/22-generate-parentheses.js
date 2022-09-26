/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    //backtracking and dfs
    let ans = [];
    function dfs(str, open, close){
        //backtracking case: number of ( is less then number of )
        if(open < close) return;
        
        //there are n number of open and close case
        if(open === n && close === n) {
            ans.push(str);
            return;
        }
        
        //dfs traversal
        if(open <n) dfs(str+"(", open+1, close);
        if(close < n) dfs(str+")", open, close+1);
    }
    dfs("", 0,0)
    return ans;
};