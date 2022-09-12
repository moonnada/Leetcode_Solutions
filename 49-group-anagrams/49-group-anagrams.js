/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    //time : o(n*klgk) where n is the length of input array and k is the maximum length of a string in input array
    //space : o(n)
    let map = new Map();
    for(let str of strs){
        let sorted = str.split("").sort().join("");
        if(map.has(sorted)) map.set(sorted , [...map.get(sorted), str])
        else map.set(sorted, [str])
    }
    return Array.from(map.values())
};