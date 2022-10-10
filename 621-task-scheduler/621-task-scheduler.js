/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function(tasks, n) {
    //the map will be our tracking mechanism
    let map = new Map();
    
    //the max occurences
    let maxVal = 0;
    
    //the number of tasks that has the max occurences
    let maxValCnt = 0;
    
    for(let k of tasks){
        let tVal = map.has(k) ? map.get(k)+1 : 1;
        map.set(k, tVal);
        //set our maxVal and number of maxVal tasks only if we have a new max
        if(tVal > maxVal){
            maxVal = tVal;
            maxValCnt = 1;
        }
        //otherwise, increment number of maxVal tasks
        else if(tVal === maxVal){
            maxValCnt++;
        }
    }
    
    return Math.max(tasks.length, (maxVal-1)*(n+1)+maxValCnt)

};