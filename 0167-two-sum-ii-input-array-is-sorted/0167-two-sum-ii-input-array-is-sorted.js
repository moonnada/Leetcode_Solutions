/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    /*
    - input arr is sorted already in increasing order
    - there is an one solution exactly
    - cant use the same element twice
    - constant extra space
    
    ex) 
           0 1 2
    arr = [2,3,4] t = 6
    => [1,3]
    
    */
    
    let left = 0;
    let right = numbers.length-1;
    while(left < right){
        if(numbers[left] + numbers[right] === target) return [left+1, right+1];
        else if(numbers[left] + numbers[right] > target) right--;
        else left++
    }
};