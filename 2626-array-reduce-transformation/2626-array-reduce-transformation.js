/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let ans = init;
    // if(nums.length === 0) return init;
    // for(const element of nums){
    //     ans = fn(ans, element);
    // }
    
    nums.forEach((element) => {
        ans = fn(ans, element)
    })
    return ans
    
};