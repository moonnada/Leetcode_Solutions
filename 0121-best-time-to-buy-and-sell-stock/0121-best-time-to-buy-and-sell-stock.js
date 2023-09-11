/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    
    /*
    ex) 
    prices = [7,1,5,3,6,4]
                  c 
                p
                
    maxProfit=4
    
    1. init a val as starting on arr[0]
    2. traverse the input arr to get the max profit
        3. check edge case which is arr[0] > arr[i] continously
        4. compare and get the max profit
    
    */
    
    let min = prices[0];
    let max = 0;
    for(let i=1; i<prices.length; i++){
        min = Math.min(min, prices[i]);
        max = Math.max(max, prices[i]-min)
    }
    return max
    
};