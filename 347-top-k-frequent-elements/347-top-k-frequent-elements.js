/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    /*
    U.
    ex.1) nums = [ 1,1,1,2,2,3], k =2 => [1,2]
    ex.2) nums = [ ] , k=2 => []
    ex.3) nums = [1,2,3] , k=3 => []
    q. is the input arr sorted?
    
    M. hashmap, bucket sort
    
    P.
    1. init values(map, bucket, ans). map[number , freq]
    2. traverse the input arr to put number as key and freq as val
    3. traverse the map to put bucket arr. 
    3.2) if bucket has same frequency, then add number into the current position, else create a new set and put the num the current position
    bucket[freq] = (bucket[freq] || new Set()).add(num)
    4. traverse the bucket to get the k most freq. start from end to 0
    4.1) put bucket element into ans num
    4.2) if ans arry lenght is the same as k, then break.
    */
    let map = new Map();
    let bucket = [];
    let ans = [];
    
    for(num of nums){
        map.set(num, (map.get(num) || 0)+1 )
    }
    
    for(let [num, freq] of map){
        bucket[freq] = (bucket[freq] || new Set()).add(num);
    }
    
    for(let i=bucket.length-1; i>=0; i--){
        if(bucket[i]) ans.push(...bucket[i])
        if(ans.length === k) break
    }
    return ans
    
    
    
//    let map = new Map();
//     let bucket = [];
//     let ans = [];
    
//     for(let num of nums){
//         map.set(num, (map.get(num) || 0) + 1);
//     }
    
//     for(let [num, freq] of map){
//         bucket[freq] = (bucket[freq] || new Set()).add(num);
//     }
    
//     for(let i=bucket.length-1; i>=0; i--){
//         if(bucket[i]) ans.push(...bucket[i])
//         if(ans.length === k) break
//     }
//     return ans
};