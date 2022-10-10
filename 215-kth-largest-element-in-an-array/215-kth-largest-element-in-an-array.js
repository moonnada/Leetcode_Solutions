/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    //quicksort
    //the final position of the kth largest number in a sorted arr
    let finalIndex = nums.length-k;
    let left = 0;
    let right = nums.length-1;
    
    while(left <= right){
        //random num between left and right
        let pivot = Math.floor(Math.random() * (right-left+1))+left;
        
        //the final position of the pivot in a sorted arr
        let pivotIndex = pivotHelper(pivot, left, right);
        
        //the target num is on the correct position, thus return
        if(pivotIndex === finalIndex) return nums[finalIndex];
        
        //if pivotIdx < finalIndex, only look on the right half
        if(pivotIndex < finalIndex) left = pivotIndex+1;
        
        //else, only look on the left half
        else right = pivotIndex-1;
    }
    
    function pivotHelper(pivot, start, end){
        //move the pivot to the end
        swap(pivot, end);
        
        let i= start;
        let j = start;
        
        //move smaller nums to the beginning of the arr
        while( j<end ){
            if(nums[j] <= nums[end]){
                swap(i,j);
                i++;
            }
            j++;
        }
        swap(i,end);
        return i;
    }
    
    function swap(i,j){
        [nums[i] , nums[j] ] = [nums[j] , nums[i]]
    }
};