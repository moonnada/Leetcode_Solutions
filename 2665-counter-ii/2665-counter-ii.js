/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let curInit = init;
    
    function increment(){
        curInit += 1;
        return curInit;
    }
    
    function decrement(){
        curInit -= 1;
        return curInit;
    }
    
    function reset(){
        return curInit = init;
    }
    
    return {increment, decrement, reset}
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */