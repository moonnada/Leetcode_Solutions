/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(T) {
    /*
        1. iterate through given array from the back.
        2. at each i, keep popping from stack until its last element is greater then cur element or empty. 
        if stack is empty, there is no greater element for cur element.
        else, stack's last element is the next greater element, so we should record the distance between current index and the index of that element. hence we will push indices into stack instead of element themselves.
        3. repeat this until the start of arr and return the result arr.
    */
//     let stack = [];
//    let result = new Array(T.length).fill(0);
//     for(let i=T.length-1; i >= 0; i--){
//         //when stack is not empty and cur val is greater or equal than stack's element
//         while(stack.length && T[i] >= T[stack[stack.length-1]]){
//          stack.pop();
//         }
//         if(stack.length){
//             console.log("stack[stack.length-1] = " + stack[stack.length-1])
//             result[i] = stack[stack.length-1] - i;   
//         }
//         stack.push(i)
//     }
//     return result;
// 
    let hottest = 0;
    let ans = new Array(T.length).fill(0);
    
    for(let curDay = T.length-1; curDay>=0; curDay--){
        let curTemp = T[curDay];
        if(curTemp >= hottest){
            hottest = curTemp;
            continue;
        }
        let days = 1;
        while(T[curDay + days] <= curTemp){
            days += ans[curDay + days];
        }
        ans[curDay] = days
    }
    return ans
};  