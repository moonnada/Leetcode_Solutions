/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function(target, position, speed) {
    //time : o(nlgn) space: o(n)
    let cars = [];
    for(let i=0; i<position.length; i++){
        cars.push({
            pos: position[i],
            speed: speed[i]
        })
    }
    
    cars.sort((a,b) => b.pos - a.pos);
    
    let stack = [];
    
    for(let i=0; i<cars.length; i++){
        const car = cars[i];
        const time = (target - car.pos) / car.speed;
        
        if(stack.length === 0 || time > stack[stack.length-1]){
            stack.push(time)
        }
    }
    return stack.length
};