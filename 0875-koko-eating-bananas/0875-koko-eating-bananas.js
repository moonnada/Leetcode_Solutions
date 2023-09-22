/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    /*
    [3,6,7,11], h = 8
    1  2 2  3
    kbanana = nums[i] / 
    => 4
    
    [30,11,23,4,20], h = 6
    */
    
    let start = 0;
    let end = Math.max(...piles);
    while(start <= end){
        let mid = Math.floor(start + (end - start) / 2);
        let hr = 0;
        for(let pile of piles){
            hr += Math.ceil(pile / mid);
        }
        
        if(hr > h) start = mid+1;
        else end = mid -1;
    }
    return start
};