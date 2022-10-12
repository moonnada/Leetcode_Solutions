/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    let bucket= [];
    let ans = [];
    backtracking(0, target);
    return ans
    function backtracking(start, target){
        if(target == 0) return ans.push([...bucket]);
        if(target < 0) return;
        if(start === candidates.length) return;
        bucket.push(candidates[start]);
        backtracking(start, target-candidates[start]);
        bucket.pop();
        backtracking(start+1, target)
    }
};