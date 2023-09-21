/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    /*
    [73,74,75,71,69,72,76,73]
           c   i
     
     if( arr[c] < arr[i]) ans.push(i-cur). cur++. break 
     if( arr[c] >= arr[i] )
    */
 let n = temperatures.length;
    let ans = new Array(n).fill(0);
    let stack = [];
    for(let i=0; i<n; i++){
        while(stack.length && temperatures[i] > temperatures[stack[stack.length-1]]){
            let idx = stack.pop();
            ans[idx] = i-idx
        }
        
        stack.push(i)
    }
    return ans
};