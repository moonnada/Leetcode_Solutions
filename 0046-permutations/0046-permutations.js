/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
   let ans = [];
    backtracking([], nums);
    return ans;
    function backtracking(cur, rem){
        if(!rem.length) ans.push([...cur]);
        for(let i=0; i<rem.length; i++){
            let newCur = rem[i];
            cur.push(newCur);
            let newRem = rem.filter((num , idx) => idx !== i);
            backtracking(cur, newRem);
            cur.pop();
        }
    }
   
};