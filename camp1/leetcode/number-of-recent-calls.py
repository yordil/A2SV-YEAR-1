class RecentCounter:

    def __init__(self):
        self.deck = deque()
        self.i = 3000
    def ping(self, t: int) -> int:
        self.deck.append(t)
        while self.deck and t - self.i > self.deck[0]:
            self.deck.popleft()
        return len(self.deck)




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)