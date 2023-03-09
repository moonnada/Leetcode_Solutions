/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    /*
    1. sort input arr
    2. init output arr
    3. traverse the sorted arr to find sum = 0
        3-1) if i > 0, then break
        3-2) if (i > 0 && curElement and curElement -1 are equal), then continue // to avoid getting the same format
        3-3) init mid and right val
        4. while (mid < right) init sum value
        5. if sum = 0, put cur three elements into arr
            6. to check there is the same element constantly for mid and right 
            7. mid++, right--;
        8. else sum > target ? right-- : mid++
        
    */
    
    const numbers = nums.sort((a,b)=> a-b);
    let ans = [];
    
    for(let i=0; i<numbers.length-2; i++){
        if(i>0 && numbers[i] === numbers[i-1]) continue;
        
        let mid = i+1;
        let right = numbers.length-1;
        while(mid < right){
            let sum = numbers[i] + numbers[mid] + numbers[right];
            if(sum === 0){
                ans.push( [numbers[i], numbers[mid], numbers[right] ]);
                 
                while(numbers[mid] === numbers[mid+1]) mid++;
                while(numbers[right] === numbers[right-1]) right--;
                
                mid++; right--;
                
            } else sum > 0 ? right-- : mid++
        }
    }
    return ans
};