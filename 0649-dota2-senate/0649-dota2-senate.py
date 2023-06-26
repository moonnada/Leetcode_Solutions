class Solution:
    def predictPartyVictory(self, senate: str) -> str:  
        
        '''
        U:
            q) input srt consists only R and S? not a lowercase too?

            ex) 'RRDRDD'

             1. RRDDR
             2. RDRR
             3. RRR

        M: queue

        P: 
            1. init two queues for each char
            2. traverse the input str to put a char's index into each queue
            3. while both queues exist
                3.1) pop both queues' left and init as a val
                3.2) compare cur positions and 
        '''
        
        senate = list(senate)
        D, R = deque(), deque()
        
        for i , c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)
                
        while D and R:
            dVal = D.popleft()
            rVal = R.popleft()
            
            if dVal < rVal:
                D.append(dVal + len(senate))
            else:
                R.append(rVal + len(senate))
                
        return "Radiant" if R else "Dire"