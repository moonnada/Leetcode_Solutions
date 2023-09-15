/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    /*
    stack
    
   if cur char is open parentheses ? put into stack
    else pop from stack and compare the cur char and popped value. if they are not matched, return false
    */
    
    let stack = [];
    for(let i=0; i<s.length; i++){
        switch(s[i]){
            case '(':
                stack.push(')');
                break;
            case '{':
                stack.push('}');
                break;
            case '[':
                stack.push(']');
                break;
            default:
                if(s[i] !== stack.pop()) return false;
                break
        }
    }
    
    return stack.length === 0
};