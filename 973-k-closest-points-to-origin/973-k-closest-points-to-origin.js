/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function(points, k) {
    /*
    MaxHeap. delete from the end.
    time: o(nlgn), space: o(n)
    */
    const heap = new MaxPriorityQueue({
        compare: (p1, p2) => p1.distance < p2.distance
    })
    
    for(let i=0; i<points.length; i++){
        const point = points[i],
              distance = Math.pow(point[0], 2) + Math.pow(point[1],2);
        heap.enqueue({point, distance});
        if(heap.size() > k) heap.dequeue();
    }
    
    return heap.toArray().map(v => v.point)
};