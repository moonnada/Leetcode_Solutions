/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    /*
    DFS
   
    */
    
    function getPreReqsPerCourse(numCourses, prerequisites){
        const prereqsPerCourse = [];
        for(let course=0; course<numCourses; course++){
            prereqsPerCourse[course] = [];
        }
        
        for(let i=0; i<prerequisites.length; i++){
            const [course, preReq] = prerequisites[i];
            prereqsPerCourse[course].push(preReq);
        }
        return prereqsPerCourse;
    }
    
    const prereqsPerCourse = getPreReqsPerCourse(numCourses, prerequisites);
    const visitedState = {
        unknown: 0,
        checkingPreReqs: 1,
        preReqMet: 2,
    }
    const visited = [];
    for(let course=0; course<numCourses; course++){
        visited[course] = visitedState.unknown;
    }
    
    function isPreReqHierarchyValid(course){
        const state = visited[course];
        if(state === visitedState.checkingPreReqs) return false;
        else if( state === visitedState.preReqMet) return true;
        else if(state === visitedState.unknown){
            visited[course] = visitedState.checkingPreReqs;
            const preReqs = prereqsPerCourse[course];
            
            for(let i=0; i<preReqs.length; i++){
                const preReq = preReqs[i];
                const isPreReqValid = isPreReqHierarchyValid(preReq);
                if(!isPreReqValid) return false;
            }
            visited[course] = visitedState.preReqMet;
            return true
        }
    }
    
    for(let course=0; course<numCourses; course++){
        const isValid = isPreReqHierarchyValid(course);
        if(!isValid) return false;
    } return true
    
};