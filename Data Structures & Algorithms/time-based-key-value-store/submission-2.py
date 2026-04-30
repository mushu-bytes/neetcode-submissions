class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # key : [(timestamp, val), ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.store[key]:
            self.store[key].append((timestamp, value))
        else:
            l, r = 0, len(self.store[key]) - 1
            while l <= r:
                m = (l + r) // 2
                if self.store[key][m][0] > timestamp:
                    r = m - 1
                elif self.store[key][m][0] < timestamp:
                    l = m + 1
                else:
                    self.store[key][m] = (timestamp, value)
                    return

    def get(self, key: str, timestamp: int) -> str:
        if not self.store[key]:
            return ""
        l, r = 0, len(self.store[key]) - 1
        target = float('inf')
        while l <= r:
            m = (l + r) // 2
            if self.store[key][m][0] <= timestamp:
                l = m + 1
                target = m
            else:
                r = m - 1

        if target == float('inf') or self.store[key][target][0] > timestamp:
            return ""
        return self.store[key][target][1]


        

        
