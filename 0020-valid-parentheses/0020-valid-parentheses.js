/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    /*
    ex) s = "[{( ) ( ) }]"
    
    stack = [, {, (
    
    1. if cur char is a open parenthese? put into stack
    2. if cur char is a closed parenthese? pop the prev char if they are match, if not return false
    */
    
    let stack = [];
    for(let i=0; i<s.length; i++){
        let curChar = s.charAt(i);
        
        switch(curChar){
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
                if(curChar !== stack.pop()) return false;
                break;
        }
    }
    
    return stack.length === 0
};