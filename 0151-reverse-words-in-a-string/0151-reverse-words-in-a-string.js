/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    const ans = [];
    let word = "";
    for(let i=0; i<s.length; i++){
        if(s.charAt(i) === " "){
            word && ans.unshift(word);
            word = "";
        } else {
            word += s.charAt(i);
        }
    }
    
    word && ans.unshift(word);
    
    return ans.join(' ');
};