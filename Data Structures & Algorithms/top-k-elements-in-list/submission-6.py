class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # need to keep a count of each element and number of occurrences
        # then we need to find the numbers at each frequency
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        freq = [ [] for i in range(len(nums) + 1)] # idx is frequency, value is nums at that freq
        for key, value in count.items():
            freq[value].append(key)

        res = []
        i = len(nums)
        while len(res) < k:
            for value in freq[i]:
                res.append(value)
            i -= 1
        return res

