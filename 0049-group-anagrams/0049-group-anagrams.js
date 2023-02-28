/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    //HashMap (key: word, val: list of the same anagram)
    /*
    1. init a map
    2. traverse the input arr
    3. sorted the cur word
    4. if map has the sorted word, the add to the list
    5. else put the cur word into the map
    6. return map.val
    */
    
    let map = new Map();
    for(let str of strs){
        let sorted = str.split("").sort().join("");
        if(map.has(sorted)) {
            map.set( sorted, [...map.get(sorted), str] )
        } else {
            map.set(sorted, [str])
        }
    }
    return Array.from(map.values())
};