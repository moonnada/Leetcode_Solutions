/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    const OPERATIONS = ["+" , "-", "*", "/"];
    let stack = [];
    for(let token of tokens){
        if(!OPERATIONS.includes(token)){
            stack.push(Number(token));
            continue;
        }
        
        const n2 = stack.pop();
        const n1 = stack.pop();
        
        switch(token){
            case "+":
                stack.push(n1+n2);
                break;
            case "-":
                stack.push(n1-n2);
                break;
            case "/":
                stack.push( Math.trunc(n1/n2));
                break;
            case "*":
                stack.push(n1*n2);
                break;
            default:
                break;
        }
    }
    return stack.pop()
};