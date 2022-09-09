/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    //Two pointers
    //time : O(n), space: o(1)
    for(let start = 0, end = numbers.length-1; start <end;){
        let sum = numbers[start] + numbers[end];
        if(sum === target){
            return [start+1 ,end+1]
        } 
        sum > target ? end-- : start++
    }
};