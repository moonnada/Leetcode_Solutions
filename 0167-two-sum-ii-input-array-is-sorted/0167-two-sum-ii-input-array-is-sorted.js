/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    /*
    Two pointers
    return their element position+1
    1. init two pointers. left and right
    2. iterative the input arr to find ans
    2. if cur two pointers sum = target, return the two pointer+1 each place
    3. else if sum>target, right--, else left++
    */
    
    let left = 0;
    let right = numbers.length-1;
    
    while(left < right){
        let sum = numbers[left] + numbers[right];
        if(sum === target){
            return [left+1, right+1];
        } 
        sum > target ? right-- : left++;
    }
};