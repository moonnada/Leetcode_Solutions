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
    
    M. hashmap
    P.
    1. init a hashmap. map [ element, frequency]
    2. traverse the input arr to put map
    3. traverse the map to find key >= k. if found push to return arr 
    */
    let map = new Map();
    for(let i=0; i<nums.length;  i++){
        // if(map.has(nums[i])){
        //     map.set(nums[i] , map.get(nums[i]) +1 );
        // } else {
        //     map.set(nums[i],1)
        // }
        map.has(nums[i]) ? map.set(nums[i], map.get(nums[i])+1) : map.set(nums[i],1);
    }
    
    let buckets = new Array(nums.length+1).fill(0).map(() => new Array(0));
    for(const [num, count] of map.entries()){
        buckets[count].push(num)
    }
    
    const ans = [];
    for( const val of buckets){
        ans.push(...val);
    }
    
    return ans.slice(ans.length-k, ans.length);
};