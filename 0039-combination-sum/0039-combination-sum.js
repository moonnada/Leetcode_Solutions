/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    let buffer = [];
    let ans = [];
    backtracking(0, target);
    return ans;
    
    function backtracking(startIndex, target){
        if(target === 0) return ans.push([...buffer]);
        if(target < 0) return;
        if(startIndex === candidates.length) return;
        buffer.push(candidates[startIndex]);
        backtracking(startIndex, target - candidates[startIndex]);
        buffer.pop();
        backtracking(startIndex+1, target)
    }
};