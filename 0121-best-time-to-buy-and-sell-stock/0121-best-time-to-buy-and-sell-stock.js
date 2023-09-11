/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    
    /*
    ex) 
    prices = [7,1,5,3,6,4]
                  
                
                
   min = 1
   max = max(prices[i] - min) = 4
    
    */
    
   let min = prices[0];
    let max = 0;
    for(let i=1; i<prices.length; i++){
        min = Math.min(min, prices[i]);
        max = Math.max(max, prices[i] - min)
    }
    return max
    
};