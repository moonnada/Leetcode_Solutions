/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    let ans = [];
    backtracking([], nums);
    return ans
    
    function backtracking(cur, rem){
        if(rem.length === 0) ans.push([...cur]);
        for(let i=0; i<rem.length; i++){
            let newCur = [...cur];
            let newRem = [...rem];
            newCur.push(newRem[i]);
            newRem.splice(i,1);
            backtracking(newCur, newRem)
        }
    }
   
};