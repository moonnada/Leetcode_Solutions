/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
   /*
   backtracking
   1. edge cases(empty)
   2. init ans arr
   3. sort the input arr
   3. init a helper func(sum, curArray, idx)
   3-1) if sum = target, then put the curArrau into ans arr
   3-2) if sum > target, then just return
   3-3) iterate over the input arr and put each element into curArr
   3-4) recursive the helper func(sum+curElement, curArr, idx+1)
   3-5) pop the curArr
   4. call helpfuc(0,[],0)
   */
    
    if(!candidates) return [];
    let ans = [];
    candidates = candidates.sort((a,b) => a-b); 
    
    function backtracking(sum, cur, idx){
        if(sum === target)  ans.push([...cur]);
        if(sum > target ) return;
        
        for(let i=idx; i<candidates.length; i++){
            if(i > idx && candidates[i-1] === candidates[i]) continue;
            cur.push(candidates[i]);
            backtracking(sum+candidates[i], cur, i+1)
            cur.pop();
        }
    }
    
    backtracking(0, [], 0);
    return ans;
}