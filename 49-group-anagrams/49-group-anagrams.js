/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    //time : o(n*klgk) where n is the length of input array and k is the maximum length of a string in input array
    //space : o(n)
    // let map = new Map();
    // for(let str of strs){
    //     let sorted = str.split("").sort().join("");
    //     if(map.has(sorted)) map.set(sorted , [...map.get(sorted), str])
    //     else map.set(sorted, [str])
    // }
    // return Array.from(map.values())
    
    //time : O(nk) space : o(n)   
      let res = {};
    for (let str of strs) {
        let count = new Array(26).fill(0);
        for (let char of str) count[char.charCodeAt()-97]++;
        let key = count.join("#");
        res[key] ? res[key].push(str) : res[key] = [str];
    }
    return Object.values(res);
};