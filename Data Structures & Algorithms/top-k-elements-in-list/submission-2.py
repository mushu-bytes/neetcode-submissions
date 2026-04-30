class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        buckets = [[] for i in range((len(nums) + 1))]
        for num, c in count.items():
            buckets[c].append(num)
        
        res = []
        for i in range(len(buckets) -1, -1, -1):
            for n in buckets[i]:
                if k == 0:
                    return res
                res.append(n)
                k -= 1
        return res
                