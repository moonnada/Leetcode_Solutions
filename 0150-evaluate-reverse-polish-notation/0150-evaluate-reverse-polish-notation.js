/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    /*
    tokens = ["4","13","5","/","+"]
    
    4 + (13/5)
    
    1. init a stack
    2. traverse the input arr to put elements
        2.1) if element is found, then put into stack
        2.2) if operator is found, then pop the two recent values from stack and save as num2, num1
                num1 operator num2
                and put back into the new value into stack
    
    */
    let stack = [];
    const OPERATIONS = ['+', '-','*', '/'];
    for(let token of tokens){
        if(!OPERATIONS.includes(token)){
            stack.push(Number(token));
            continue;
        }
        
        const n2 = stack.pop();
        const n1 = stack.pop();
        
        switch(token){
            case '+':
                stack.push(n1+n2);
                break;
            case '-':
                stack.push(n1-n2);
                break;
            case '*':
                stack.push(n1*n2);
                break;
            case '/':
                stack.push(Math.trunc(n1/n2));
                break;
            default:
                break;
        }
    }
    return stack.pop()
};