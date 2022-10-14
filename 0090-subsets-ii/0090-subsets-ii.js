/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    /*
    backtracking
    1. sort input arr
    2. init ans arr
    3. start backtracking func from 0 and empty arr
    4. in the backtracking func, traverse the input arr, so i can find it's possible values
    5. check whether duplicate num exists. if is, then just continue. ex) nums[i-1] === num[i], 
    6. init val to get curVal
    7. choose step. I can start with the index val, so that i can find the next combined possible values for the 0th val
    8. explore step. recursive 
    9. unchoose step. pop the val, so can start with other val
    10. return ans
    */
   
    nums = nums.sort((a,b) => a-b);
    let ans = [[]];
    backtracking(0,[]);
    return ans;
    
    function backtracking(first, cur){
        for(let i=first; i<nums.length; i++){
            if(i > first && nums[i-1] === nums[i]) continue;
            let newCur = nums[i];
            cur.push(newCur);
            ans.push([...cur]);
            backtracking(i+1, cur)
            cur.pop();
        }
    }
};