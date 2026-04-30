class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for key, value in counter.items():
            buckets[value].append(key)

        kfreq = []
        for r in range(len(buckets) - 1, -1, -1):
            if not buckets[r]:
                continue
            for num in buckets[r]:
                kfreq.append(num)
                if len(kfreq) == k:
                    return kfreq