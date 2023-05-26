/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    /*
    U: 
        q) any letters can be in input strs?
    M: map (key: str, val: arr of str)
    P: 
     1. init a map 
     2. traverse the input strs of each char into map
        2.1) sort a current str
        2.2) if a str is already in a map, put into map
        2.3) else put the cur str into map
    */
    
    let map = new Map();
    for(let str of strs){
        let sortedStr = str.split("").sort().join("");
        if(map.has(sortedStr)){
            map.set(sortedStr, [...map.get(sortedStr), str] )
        } else {
            map.set(sortedStr, [str])
        }
    }
    return Array.from(map.values())
};