class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        myt = deque(tickets)
        time = 0

        while myt:
            if myt[0] > 0:
                myt[0] -= 1
                time += 1

                if myt[k] == 0:
                    return time

            myt.append(myt.popleft())
            k = (k - 1) % len(myt)

        return time