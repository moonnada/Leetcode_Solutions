/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    /*
    s = "3[a2[c]]"
    
    acc
    
    stack
    
   
    */
    const stack = [];
    for(const char of s){
        if(char !== "]"){
            stack.push(char);
            continue;
        }
        let curChar = stack.pop();
        let str = "";
        
        while(curChar !== '['){
            str = curChar + str;
            curChar = stack.pop();
        }
         
        let num = '';
        curChar = stack.pop();
        while(!Number.isNaN(Number(curChar))){
            num = curChar + num;
            curChar = stack.pop();
        }
        
        stack.push(curChar);
        stack.push(str.repeat(Number(num)))
    }
    return stack.join('')
    
};