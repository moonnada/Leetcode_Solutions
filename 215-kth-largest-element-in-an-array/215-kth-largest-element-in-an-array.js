/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    let finalIndex = nums.length -k;
    let left = 0;
    let right = nums.length-1;
    
    while(left<= right){
        //random num between left and right
        const pivot = Math.floor(Math.random() * (right - left + 1)) + left;
        
        //the final position of the pivot in a sorted arr
        const pivotIndex = pivotHelper(pivot, left, right);
        
        //the target num is in its correct position, thus reutn
        if(pivotIndex === finalIndex) return nums[finalIndex];
        
        //if pivotIndex is smaller than finalIndex, only look the right half
        if(pivotIndex < finalIndex) left = pivotIndex+1;
        else right = pivotIndex-1;
    }
    
    function pivotHelper(pivot, start, end){
        //move the pivot to the end
        swap(pivot, end);
        
        let i = start;
        let j = start;
        while(j<end){
            if(nums[j] <= nums[end]){
                swap(i,j)
                i++;
            }
            j++;
        }
        
        swap(i,end);
        return i;
    }
    
    function swap(i,j){
        [nums[i], nums[j]] = [nums[j], nums[i]]
    }
};