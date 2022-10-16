/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    /*
    1. init ans and partitions
    2. check a str is palindrom
    3. in a helpfunc, 
    */
    let ans = [];
    let partitions = [];
    let isPalindrom = str => str === str.split('').reverse().join('');
    
    function findPalindrom(str, start, parts, result){
        if(start === str.length){
           return result.push([...parts]);
           
        }
        
        for(let i=start+1; i<=str.length; i++){
            let target = str.substring(start, i);
            if(isPalindrom(target)){
                parts.push(target);
                findPalindrom(str, i, parts, result);
                parts.pop();
            }
        }
    }
    
    findPalindrom(s, 0, partitions, ans);
    return ans
    
    
};