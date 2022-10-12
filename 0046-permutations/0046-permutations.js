/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    let ans = [];
    function backtracking(cur, rem){
        if(rem.length <= 0) ans.push([...cur]);
        else {
            for(let i=0; i<rem.length; i++){
                cur.push(rem[i]);
                backtracking([...cur], rem.slice(0,i).concat(rem.slice(i+1)));
                cur.pop();
            }
        }
    }
    backtracking([], nums);
    return ans
};