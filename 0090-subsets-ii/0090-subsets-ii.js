/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    nums = nums.sort((a,b) => a-b);
    let ans = [[]];
    backtracking(0,[]);
    return ans;
    
    function backtracking(first, cur){
        for(let i=first; i<nums.length; i++){
            if(i> first &&nums[i-1] === nums[i]) continue;
            cur.push(nums[i]);
            ans.push([...cur])
            backtracking(i+1, cur);
            cur.pop()
        }
    }
    
   
};