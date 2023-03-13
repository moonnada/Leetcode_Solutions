/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    /*
    1. traverse the input arr
    2. get min val between (i and i+1)
    3. if n[i+1] > n[i], calculate profit.
    4. set profit as max if new profit is larger
    */
    
    let max = 0;
    let min = prices[0];
    
    for(let i=1; i<prices.length; i++){
        min = Math.min(min, prices[i]);
        max = Math.max(max, prices[i]-min)      
    }
    return max
};