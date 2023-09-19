/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];
    for(let i=0; i<s.length; i++){
        let curVal = s[i];
        
        switch(curVal){
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
                        if(stack.pop() !== curVal) return false;
                        break;
                    
        }
           
        
    }
        
        return stack.length === 0
};