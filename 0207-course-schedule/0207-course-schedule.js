/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    let preMap = {};
    let visited = {};
    
    
    for(let i=0; i<prerequisites.length; i++){
        if(preMap[prerequisites[i][0]] === undefined){
            preMap[prerequisites[i][0]] = [prerequisites[i][1]];
        } else {
            preMap[prerequisites[i][0]].push(prerequisites[i][1]);
        }
    }
    
    function dfs(node){
        //if already visit the cur node, return false
        if(visited[node]) return false;
        
        //if cur node has not visited yet
        if(preMap[node] !== undefined){
            
            //if curNode of map is empty (means reaching the end of node), return true
            if(preMap[node].length === 0) return true;
            
            //mark cur node as visited
            visited[node] = true;
            
            //traverse curNode of map to see there is no re-occurance of the curNode.
            //if dfs func returns false, then return false
            for(let val of preMap[node]){
                if(!dfs(val)) return false;
            }
            
            visited[node] = false;
            preMap[node] = [];
        }
        return true;
    }
    
    for(let key in preMap){
        //if dfs func returns false, then return false
        if(!dfs(key)) return false;
    }
    return true;
};