/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function(target, position, speed) {
    /*
    target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    
    
    */
    
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
        
        if(stack.length === 0 || time > stack[stack.length -1]){
            stack.push(time)
        }
    }
    return stack.length
};