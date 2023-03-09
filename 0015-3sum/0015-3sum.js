/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
     // sort for simpler detection of duplicates
    const numbers = nums.sort((a, b) => a - b);

    const triplets = [];
    for (let i = 0; i < numbers.length; i++) {
        // prevent duplicates
        if (i > 0 && numbers[i - 1] === numbers[i]) {
            continue;
        }

        // find sum with 2-pointer method
        let left = i + 1;
        let right = numbers.length - 1;
        while (left < right) {
            const sum = numbers[i] + numbers[left] + numbers[right];
            if (sum === 0) {
                triplets.push([numbers[i], numbers[left], numbers[right]]);
                // shift pointer to a new value to prevent duplicates
                left++;
                while (numbers[left] === numbers[left - 1] && left < right) {
                    left++;
                }
            } else if (sum > 0) {
                right--;
            } else {
                left++;
            }
        }
    }

    return triplets;
};