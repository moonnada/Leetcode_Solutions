/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    if(!candidates || candidates.length === 0) return [];   
    let ans = [];
    candidates = candidates.sort((a,b) => a-b);
    
    function backtracking(curSum, cur, idx){
        if(curSum === target) return ans.push([...cur]);
        
        for(let i=idx; i<candidates.length; i++){
            if( i != idx && candidates[i] === candidates[i-1]) continue;
            if(curSum > target) return;
            
            cur.push(candidates[i]);
            backtracking(curSum + candidates[i], cur, i+1)
            cur.pop();
        }
        
    }
    
    backtracking(0, [] , 0);
    return ans;
}