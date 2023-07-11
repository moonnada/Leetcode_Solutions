class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        '''
        U:
            ex) [ [1,2] , [2,3] , [0] , [1]]]]\
        
        M: stack
        
        P:
            1. init a set and stack
            2. while stack exists
                2.1) pop cur val from stack
                2.2) put the curval into set
                2.3) looping the input list to visit each index with curval
                    2.4) if key is not in set, put into stack
            3. return true if len of input list and set equal
        '''
        
        visitedRoom = set()
        stack = [0]
        
        while stack:
            room = stack.pop()
            visitedRoom.add(room)
            
            for key in rooms[room]:
                if not key in visitedRoom:
                    stack.append(key)

        return len(rooms) == len(visitedRoom)
            