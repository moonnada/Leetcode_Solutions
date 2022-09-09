/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
   /*
   arr = [-1,0,1,2,-1,-4]
   1. sort the input arr. [-4,-1,-1,0,1,2]
   2. init a target val as 0
   3. traverse the sorted arr from 0 to length-2. the reason length-2 is I am going to add the right pointer as nums.length -1 later
   4. check if cur element > target, then break the loop. if cur element is a postive num, can't get the sum is 0
   5. check if there is a duplicate element constantly, then continue. the reason is to escape getting a same format 
   6. init the mid and right value
   7. while(mid < right), init sum val = n[i] + n[j] + n[k]
   8. if sum = target, then put the element into output arr
   9.   also check there is same element constantly or not on mid place and right place both.
   10. mid is incremented and right is decremented
   10. else sum > target, right--, else mid++
   
   */
    
    let ans = [];
    let target = 0;
    nums.sort((a,b) => a-b);
    for(let i=0; i<nums.length-2; i++){
        if(nums[i] > target) break;
        if(i> 0 && nums[i] === nums[i-1]) continue;
        
        let j = i+1;
        let k = nums.length-1;
        while(j<k){
            let sum = nums[i] + nums[j] + nums[k];
            if(sum === target){
                ans.push([nums[i], nums[j], nums[k]]);
                
                while(nums[j]=== nums[j+1]) j++;
                while(nums[k] === nums[k-1]) k--;
                
                j++;
                k--;
            }
            else {
                sum > target ? k-- : j++;
            }
        }
    }
    return ans
}