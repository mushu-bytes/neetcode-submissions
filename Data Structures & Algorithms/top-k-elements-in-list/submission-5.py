class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        buckets = [[] for i in range(len(nums) + 1)]
        for key, val in counts.items():
            buckets[val].append(key)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i] == []:
                continue
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res