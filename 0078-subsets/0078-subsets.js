/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
   //backtracking
    let ans = [[]];
    function backtrack(first, cur){
        for(let i=first; i<nums.length; i++){
            cur.push(nums[i]);
            ans.push([...cur]);
            backtrack(i+1, cur);
            cur.pop();
            
        }
    }
    
    backtrack(0,[]);
    return ans;
};