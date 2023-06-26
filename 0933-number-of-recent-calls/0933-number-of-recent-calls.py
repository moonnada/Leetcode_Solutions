class RecentCounter:
    '''
    U:
        
    '''
    
    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] + 3000 < t:
            self.queue.pop(0)
        self.queue.append(t)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)