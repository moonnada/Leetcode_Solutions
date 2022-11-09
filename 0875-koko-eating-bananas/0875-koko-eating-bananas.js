/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    /*
    [30,11,23,4,20] , h = 6.
    
    Binary.  //time : O(nlgm). n be the length of the input array, m be the maximum number of bananas
    1. init start and end val. ex) start = 1, end = 30
    2. while start <= end
    2-1) get mid val between start and end. ex) (1+30)/2 = 15
            init a hrs val. 
    2-2) iterative a loop to get hrs by using the ceil() function. hrs += ceil(each pile / mid)
    2-3) if hrs > h, end = mid -1, else start = mid +1
    */
    
    let start =1;
    let end = Math.max(...piles);
    
    while(start <= end){
        let mid = Math.floor((start + end) / 2);
        let hrs = 0;
        for(let pile of piles){
            hrs += Math.ceil(pile / mid);
        }
        if(hrs > h) start = mid+1;
        else end = mid -1
    }
    return start
};