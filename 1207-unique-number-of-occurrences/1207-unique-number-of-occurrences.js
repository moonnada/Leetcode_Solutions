/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    /*
    U:
        - if the number of occurrences of each val is unique => true
          else false
         
         ex) [1,2,2,1,1,3]
         1:3
         2:2
         3:1
         
         ex) [-3,0,1,-3,1,1,1,-3,10,0]
         
         -3: 3
         0: 2
         1: 4
         10:1
         
         - arr can contain negative values
         - 
    M: hashmap(key-> element, value->occurrences)
    
    P: 
        1. check edge cases(null, one element)
        2. init a hashmap
        3. iterative the input arr to put key and value into map
        4. iterative the map to check occurrences. if there are not unique, return false
        5. return true
        
    time: o(n), space:o(n)
    */
    
    let map = new Map();
    
    for(let i=0; i<arr.length; i++){
//         if(map.has(num)){
//             map.set(num, (map.get(num)+1));
//         } else {
//             map.set(num, 1)
//         }
        
        map.set(arr[i], map.get(arr[i])+1 || 1);
        
    }
    
    let set = new Set(map.values());
    return set.size == map.size
    
    
};