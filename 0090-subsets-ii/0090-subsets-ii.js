/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    nums = nums.sort((a,b) => a-b);
    let ans = [];
    backtracking(nums, [], 0);
    return ans;
    
    function backtracking(nums, subSets, idx){
        ans.push([...subSets]);
        for(let i=idx; i<nums.length; i++){
            if(i>idx && nums[i-1] === nums[i]) continue;
            let newCur = nums[i];
            subSets.push(newCur);
            backtracking(nums, subSets, i+1);
            subSets.pop();
        }
    }
};