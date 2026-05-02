class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.map[key]) - 1
        print(f"Timestamp {timestamp}")
        # [1, 3]
        res = -1 

        while l <= r:
            m = (l + r) // 2
            if self.map[key][m][0] <= timestamp:
                res = m
                l = m + 1
            else:
                r = m - 1

        return self.map[key][res][1] if res != -1 else ""
